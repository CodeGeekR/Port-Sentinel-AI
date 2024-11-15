# Port-Sentinel-AI

![Port-Sentinel-AI](https://img.shields.io/badge/AI-Cyber%20Security-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen)

## Descripción

**Port Sentinel AI** es una herramienta de ciberseguridad para macOS que permite escanear y proteger los puertos abiertos en tu equipo local y router. La herramienta no solo detecta puertos inseguros, sino que también proporciona la capacidad de cerrarlos automáticamente y ofrece recomendaciones de seguridad específicas para cada puerto vulnerable detectado.

## Características

- **Escaneo Dual**: Detecta simultáneamente puertos abiertos en el equipo local y router
- **Detección de Vulnerabilidades**: Identifica 12 tipos diferentes de puertos inseguros comunes
- **Gestión Automatizada**: Cierre automático de puertos inseguros con privilegios de superusuario
- **Interfaz Amigable**: Mensajes con código de colores para mejor visualización de alertas
- **Compatibilidad macOS**: Comandos específicos para gestión de servicios en macOS
- **Ejecución Paralela**: Utiliza multithreading para escaneo rápido de puertos

## Instalación

1. Clona este repositorio:

   ```sh
   git clone https://github.com/CodeGeekR/Port-Sentinel-AI.git
   cd Port-Sentinel-AI
   ```

2. Instala las dependencias necesarias:

   ```sh
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta el script:

   ```sh
   sudo python scan.py
   ```

2. Sigue las instrucciones en pantalla para ver los puertos abiertos y recibir recomendaciones de seguridad.

## Ejemplo de Salida

```plaintext
Escaneando puertos abiertos en el router: 192.168.1.1

Puertos abiertos encontrados en el router:
Puerto 80 (http) está abierto en el router.

¡ALERTAS DE SEGURIDAD para router!
El puerto 80 es inseguro (HTTP). Se recomienda cerrarlo o asegurar su uso.

Escaneando puertos abiertos en el equipo local: 192.168.1.2

Puertos abiertos encontrados en el equipo local:
Puerto 445 (microsoft-ds) está abierto en el equipo local.

¡ALERTAS DE SEGURIDAD para equipo local!
El puerto 445 es inseguro (Microsoft-DS SMB file sharing). Se recomienda cerrarlo o asegurar su uso.

Se detectaron los siguientes puertos inseguros:
Puerto 445: SMB - Deshabilitar compartición SMB

¿Desea cerrar estos puertos? (s/N):
```

## Puertos Monitoreados

El script monitorea los siguientes puertos inseguros:

20, 21 (FTP)
23 (Telnet)
25 (SMTP)
69 (TFTP)
80 (HTTP)
110 (POP3)
143 (IMAP)
445 (SMB)
3389 (Remote Desktop)
5800, 5900 (VNC)

## Contribución

¡Las contribuciones son bienvenidas! Si deseas mejorar Port-Sentinel-AI, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y haz commit (git commit -am 'Añadir nueva funcionalidad').
4. Envía tus cambios (git push origin feature/nueva-funcionalidad).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](https://es.wikipedia.org/wiki/Licencia_MIT) para más detalles.

## Contacto

Para consultas comerciales o colaboraciones, por favor contacta a:

[![Website](https://img.shields.io/badge/Website-Visit%20My%20Portfolio-blue?style=flat-square&logo=google-chrome)](https://www.samuraidev.engineer/)
[![Email](https://img.shields.io/badge/Email-Contact%20Me-blue?style=flat-square&logo=gmail)](mailto:sammydn7@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect%20with%20Me-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/samuraidev/)

## Palabras Clave

AI
Ciberseguridad
Azure
Puertos
Escaneo
Vigilancia
Inteligencia Artificial
Protección

## Agradecimientos

Agradecemos a la comunidad de desarrolladores y a las empresas que apoyan proyectos de ciberseguridad y protección de datos.

¡Gracias por usar Port-Sentinel-AI! Si encuentras útil esta herramienta, no olvides darle una estrella ⭐ en GitHub y compartirla con tus colegas.

## Referencias

- <a href="https://es.wikipedia.org/wiki/Modelo_TCP/IP" target="_blank" rel="noopener noreferrer">Puertos TCP y UDP</a>
- <a href="https://es.wikipedia.org/wiki/Ciberseguridad" target="_blank" rel="noopener noreferrer">Ciberseguridad</a>
- <a href="https://es.wikipedia.org/wiki/Protecci%C3%B3n_de_datos" target="_blank" rel="noopener noreferrer">Protección de Datos</a>
- <a href="https://es.wikipedia.org/wiki/Inteligencia_artificial" target="_blank" rel="noopener noreferrer">Inteligencia Artificial</a>
- <a href="https://es.wikipedia.org/wiki/Esc%C3%A1ner_de_puertos" target="_blank" rel="noopener noreferrer">Escaneo de Puertos</a>
