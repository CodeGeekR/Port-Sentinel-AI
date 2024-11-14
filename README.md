# Port-Sentinel-AI

![Port-Sentinel-AI](https://img.shields.io/badge/AI-Cyber%20Security-blue)
![Azure](https://img.shields.io/badge/Azure-Cloud-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen)

## Descripción

**Port-Sentinel-AI** es una herramienta avanzada de ciberseguridad que utiliza inteligencia artificial para escanear y proteger los puertos abiertos en tu equipo local y en tu router. Con la integración de modelos LLM como GPT-4o mini de Azure, **Port-Sentinel-AI** no solo detecta puertos inseguros, sino que también proporciona recomendaciones detalladas y guías paso a paso para cerrar estos puertos y proteger tu sistema contra accesos no autorizados.

## Características

- **Escaneo de Puertos**: Detecta puertos abiertos en tu equipo local y en tu router.
- **Identificación de Puertos Inseguros**: Reconoce puertos comúnmente vulnerables y proporciona alertas.
- **Recomendaciones de Seguridad**: Utiliza AI para generar recomendaciones personalizadas sobre cómo cerrar puertos inseguros.
- **Guías Paso a Paso**: Ofrece instrucciones detalladas para proteger tu equipo.
- **Integración con Azure**: Aprovecha la potencia de los modelos LLM de Azure para análisis y recomendaciones.

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
   python scan.py
   ```

2. Sigue las instrucciones en pantalla para ver los puertos abiertos y recibir recomendaciones de seguridad.

## Ejemplo de Salida

```plaintext
Escaneando puertos abiertos en el router: 192.168.1.1

Puertos abiertos encontrados en el router:
Puerto 80 (http) está abierto en el router.
El puerto 80 es inseguro (HTTP). Se recomienda cerrarlo o asegurar su uso.

Escaneando puertos abiertos en el equipo local: 192.168.1.2

Puertos abiertos encontrados en el equipo local:
Puerto 445 (microsoft-ds) está abierto en el equipo local.
El puerto 445 es inseguro (Microsoft-DS SMB file sharing). Se recomienda cerrarlo o asegurar su uso.
```

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

- [Azure AI Services](https://azure.microsoft.com/en-us/services/cognitive-services/)
- [Puertos TCP y UDP](https://es.wikipedia.org/wiki/Modelo_TCP/IP)
- [Ciberseguridad](https://es.wikipedia.org/wiki/Ciberseguridad)
- [Protección de Datos](https://es.wikipedia.org/wiki/Protecci%C3%B3n_de_datos)
- [Inteligencia Artificial](https://es.wikipedia.org/wiki/Inteligencia_artificial)
- [Escaneo de Puertos](https://es.wikipedia.org/wiki/Esc%C3%A1ner_de_puertos)
