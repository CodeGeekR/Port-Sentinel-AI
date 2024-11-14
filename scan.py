import socket
from scapy.all import sr1, IP, TCP
import concurrent.futures
import netifaces

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

def get_router_ip():
    """
    Obtiene la dirección IP del router al que está conectado el dispositivo.

    Returns:
        str: La dirección IP del router.
    """
    gateways = netifaces.gateways()
    router_ip = gateways['default'][netifaces.AF_INET][0]
    return router_ip

def scan_port(ip_address, port):
    """
    Escanea un puerto específico en el host dado.

    Args:
        ip_address (str): La dirección IP del host a escanear.
        port (int): El número de puerto a escanear.

    Returns:
        bool: True si el puerto está abierto, False en caso contrario.
    """
    packet = IP(dst=ip_address) / TCP(dport=port, flags='S')
    response = sr1(packet, timeout=0.3, verbose=0)
    if response is None:
        return False
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
        return True
    else:
        return False

def scan_open_ports(ip_address, port_range=(1, 1024)):
    """
    Escanea los puertos abiertos en un host dado y obtiene su servicio.

    Args:
        ip_address (str): La dirección IP del host a escanear.
        port_range (tuple): Rango de puertos a escanear.

    Returns:
        list: Lista de tuplas con el número de puerto y su servicio.
    """
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
                pass  # Omitimos errores individuales para acelerar el proceso

    return open_ports

def main():
    try:
        # Obtener la IP del router
        router_ip = get_router_ip()
        print(f"Escaneando puertos abiertos en el router: {router_ip}")

        # Escanear puertos abiertos en el router
        open_ports_router = scan_open_ports(router_ip)
        if open_ports_router:
            print("\nPuertos abiertos encontrados en el router:")
            for port, service in sorted(open_ports_router):
                mensaje = f"Puerto {port} ({service}) está abierto en el router."
                if port in INSECURE_PORTS:
                    recomendacion = (
                        f"El puerto {port} es inseguro ({INSECURE_PORTS[port]}). "
                        "Se recomienda cerrarlo o asegurar su uso."
                    )
                    print(f"{mensaje}\n{recomendacion}\n")
                else:
                    print(mensaje)
        else:
            print("No se encontraron puertos abiertos en el router.")

        # Obtener la IP local del equipo
        local_ip = socket.gethostbyname(socket.gethostname())
        print(f"\nEscaneando puertos abiertos en el equipo local: {local_ip}")

        # Escanear puertos abiertos en el equipo local
        open_ports_local = scan_open_ports(local_ip)
        if open_ports_local:
            print("\nPuertos abiertos encontrados en el equipo local:")
            for port, service in sorted(open_ports_local):
                mensaje = f"Puerto {port} ({service}) está abierto en el equipo local."
                if port in INSECURE_PORTS:
                    recomendacion = (
                        f"El puerto {port} es inseguro ({INSECURE_PORTS[port]}). "
                        "Se recomienda cerrarlo o asegurar su uso."
                    )
                    print(f"{mensaje}\n{recomendacion}\n")
                else:
                    print(mensaje)
        else:
            print("No se encontraron puertos abiertos en el equipo local.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()