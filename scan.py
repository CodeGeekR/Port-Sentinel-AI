import socket
from scapy.all import sr1, IP, TCP
import concurrent.futures
import netifaces
import subprocess
import sys
import getpass
import os

# Códigos ANSI para colores
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

INSECURE_PORTS = {
    20: "FTP Data",
    21: "FTP Control",
    23: "Telnet",
    25: "SMTP",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    445: "Microsoft-DS SMB file sharing",
    3389: "Remote Desktop",
    5800: "VNC",
    5900: "VNC",
}

# Diccionario de puertos inseguros y comandos para cerrarlos en macOS
PORT_COMMANDS = {
    20: {
        'service': "FTP Data",
        'command': "sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add /usr/libexec/ftpd --block",
        'description': "Bloquear FTP Data"
    },
    21: {
        'service': "FTP Control",
        'command': "sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add /usr/libexec/ftpd --block",
        'description': "Bloquear FTP Control"
    },
    23: {
        'service': "Telnet",
        'command': "sudo launchctl unload -w /System/Library/LaunchDaemons/telnet.plist 2>/dev/null || true",
        'description': "Deshabilitar Telnet"
    },
    25: {
        'service': "SMTP",
        'command': "sudo postfix stop && sudo launchctl unload -w /System/Library/LaunchDaemons/org.postfix.master.plist",
        'description': "Detener servicio SMTP"
    },
    69: {
        'service': "TFTP",
        'command': "sudo launchctl unload -w /System/Library/LaunchDaemons/tftp.plist 2>/dev/null || true",
        'description': "Deshabilitar TFTP"
    },
    80: {
        'service': "HTTP",
        'command': "sudo apachectl stop && sudo launchctl unload -w /System/Library/LaunchDaemons/org.apache.httpd.plist 2>/dev/null || true",
        'description': "Detener servidor HTTP"
    },
    110: {
        'service': "POP3",
        'command': "sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add /usr/sbin/pop3d --block",
        'description': "Bloquear POP3"
    },
    143: {
        'service': "IMAP",
        'command': "sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add /usr/sbin/imapd --block",
        'description': "Bloquear IMAP"
    },
    445: {
        'service': "SMB",
        'command': "sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.smbd.plist",
        'description': "Deshabilitar compartición SMB"
    },
    3389: {
        'service': "Remote Desktop",
        'command': "sudo /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Resources/kickstart -deactivate -configure -access -off",
        'description': "Deshabilitar Acceso Remoto"
    },
    5800: {
        'service': "VNC",
        'command': "sudo /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Resources/kickstart -deactivate -configure -access -off",
        'description': "Deshabilitar VNC"
    },
    5900: {
        'service': "VNC",
        'command': "sudo /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Resources/kickstart -deactivate -configure -access -off",
        'description': "Deshabilitar VNC"
    }
}

def get_router_ip():
    """Obtiene la dirección IP del router."""
    gateways = netifaces.gateways()
    router_ip = gateways['default'][netifaces.AF_INET][0]
    return router_ip

def get_local_ip():
    """
    Obtiene la dirección IP real del equipo local.
    
    Returns:
        str: Dirección IP local del equipo
    """
    try:
        # Crear socket y conectar a un servidor externo para obtener IP real
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        # Método alternativo usando netifaces
        interfaces = netifaces.interfaces()
        for iface in interfaces:
            addrs = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in addrs:
                for addr in addrs[netifaces.AF_INET]:
                    ip = addr['addr']
                    # Excluir localhost y direcciones especiales
                    if not ip.startswith('127.') and not ip.startswith('169.254.'):
                        return ip
    return None

def scan_port(ip_address, port):
    """Escanea un puerto específico."""
    packet = IP(dst=ip_address) / TCP(dport=port, flags='S')
    response = sr1(packet, timeout=0.3, verbose=0)
    if response is None:
        return False
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
        return True
    else:
        return False

def scan_open_ports(ip_address, port_range=(1, 1024)):
    """Escanea los puertos abiertos en un host."""
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(scan_port, ip_address, port): port
            for port in range(*port_range)
        }
        for future in concurrent.futures.as_completed(futures):
            port = futures[future]
            try:
                if future.result():
                    try:
                        service = socket.getservbyport(port, 'tcp')
                    except OSError:
                        service = "Desconocido"
                    open_ports.append((port, service))
            except Exception:
                pass
    return open_ports

def show_security_alerts(open_ports, host_type):
    """Muestra las alertas de seguridad para puertos inseguros."""
    insecure_ports = [
        (port, service) for port, service in open_ports 
        if port in INSECURE_PORTS
    ]
    
    if insecure_ports:
        print(f"\n{RED}¡ALERTAS DE SEGURIDAD para {host_type}!{RESET}")
        for port, service in sorted(insecure_ports):
            print(f"{RED}El puerto {port} es inseguro ({INSECURE_PORTS[port]}). "
                f"Se recomienda cerrarlo o asegurar su uso.{RESET}")
            
def close_port(port):
    """Cierra un puerto específico usando el comando correspondiente."""
    if port not in PORT_COMMANDS:
        return False, f"No hay comando disponible para cerrar el puerto {port}"
    
    try:
        command = PORT_COMMANDS[port]['command']
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True, f"Puerto {port} ({PORT_COMMANDS[port]['service']}) cerrado exitosamente"
    except subprocess.CalledProcessError as e:
        return False, f"Error al cerrar puerto {port}: {e}"

def handle_insecure_ports(open_ports):
    """Maneja el cierre de puertos inseguros detectados."""
    insecure_ports = [port for port, _ in open_ports if port in PORT_COMMANDS]
    
    if not insecure_ports:
        return
    
    print(f"\n{YELLOW}Se detectaron los siguientes puertos inseguros:{RESET}")
    for port in insecure_ports:
        print(f"{RED}Puerto {port}: {PORT_COMMANDS[port]['service']} - {PORT_COMMANDS[port]['description']}{RESET}")
    
    response = input(f"\n{YELLOW}¿Desea cerrar estos puertos? (s/N): {RESET}").lower()
    
    if response == 's':
        print("\nCerrando puertos inseguros...")
        for port in insecure_ports:
            success, message = close_port(port)
            if success:
                print(f"{GREEN}{message}{RESET}")
            else:
                print(f"{RED}{message}{RESET}")

def main():
    try:
        # Escaneo del router
        router_ip = get_router_ip()
        print(f"Escaneando puertos abiertos en el router: {router_ip}")
        
        open_ports_router = scan_open_ports(router_ip)
        if open_ports_router:
            print("\nPuertos abiertos encontrados en el router:")
            for port, service in sorted(open_ports_router):
                print(f"Puerto {port} ({service}) está abierto en el router.")
            show_security_alerts(open_ports_router, "router")
        else:
            print("No se encontraron puertos abiertos en el router.")

        # Escaneo del equipo local usando la nueva función
        local_ip = get_local_ip()
        if not local_ip:
            raise Exception("No se pudo determinar la IP local del equipo")
            
        print(f"\nEscaneando puertos abiertos en el equipo local: {local_ip}")
        
        open_ports_local = scan_open_ports(local_ip)
        if open_ports_local:
            print("\nPuertos abiertos encontrados en el equipo local:")
            for port, service in sorted(open_ports_local):
                print(f"Puerto {port} ({service}) está abierto en el equipo local.")
            show_security_alerts(open_ports_local, "equipo local")
        else:
            print("No se encontraron puertos abiertos en el equipo local.")

        if open_ports_local:
            handle_insecure_ports(open_ports_local)
            
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

if __name__ == "__main__":
    # Verificar privilegios de superusuario
    if os.geteuid() != 0:
        print(f"{RED}Este script debe ejecutarse con privilegios de superusuario.{RESET}")
        print("Por favor, ejecute: sudo python3 scan.py")
        sys.exit(1)
    main()