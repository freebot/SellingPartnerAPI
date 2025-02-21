OAuth Authorization Code Fetcher  

  

  

Este proyecto es una aplicación web simple diseñada para obtener el código de autorización  de Amazon Selling Partner API (SP-API) y mostrarlo en pantalla para su uso posterior. La aplicación se ejecuta en un servidor Flask dentro de un contenedor Docker, lo que facilita su implementación y uso 

. 
Tabla de Contenidos  

    Descripción del Proyecto 
    Características Principales 
    Requisitos Previos 
    Instalación 
    Uso 
    Configuración de ngrok 
    Contribuciones 
    Licencia 
     

Descripción del Proyecto  

Esta aplicación actúa como un intermediario para obtener el código de autorización  necesario para interactuar con la API de Amazon SP-API. Una vez que el vendedor autoriza la aplicación, el código se muestra en pantalla para ser copiado y utilizado en tu aplicación principal 

. 

El servidor utiliza Flask para manejar las solicitudes y respuestas, y ngrok para exponer el servidor local a Internet, cumpliendo con los requisitos de Amazon para el URI de callback. 
Características Principales  

    Interfaz simple : Redirige al vendedor a Amazon para autorización y muestra el código de autorización en pantalla.
    Compatibilidad con Docker : Fácil de implementar en cualquier entorno utilizando contenedores Docker.
    Soporte para ngrok : Permite exponer el servidor local a Internet sin necesidad de configurar un servidor público.
    Ligero y eficiente : Construido con Flask, un framework Python minimalista 

    .
     

Requisitos Previos  

Antes de ejecutar esta aplicación, asegúrate de tener instalado lo siguiente: 

    Docker : Para construir y ejecutar el contenedor.
    ngrok : Para exponer el servidor local a Internet.
    Credenciales de Amazon SP-API : Necesitarás un client_id válido registrado en el Portal de Proveedores de Soluciones de Amazon.
     

Instalación  

    Clona este repositorio: 
    bash
     

 
1
2
git clone https://github.com/tu-usuario/oauth-authorization-fetcher.git
cd oauth-authorization-fetcher
 
 

Construye la imagen Docker: 
bash
 
 
1
docker build -t oauth-server .
 
 

Ejecuta el contenedor: 
bash
 

     
    1
    docker run -d -p 5000:5000 --name oauth-server oauth-server
     
     

    Verifica que el servidor esté funcionando:
    Abre un navegador y navega a http://localhost:5000. 
     

Uso  

    Navega a http://localhost:5000 en tu navegador.
    Serás redirigido a Amazon para autorizar la aplicación.
    Después de autorizar, Amazon redirigirá al vendedor a tu servidor Flask.
    La página mostrará el código de autorización  en pantalla. Cópialo y úsalo en tu aplicación para intercambiarlo por tokens.
     

Configuración de ngrok  

Amazon requiere que el URI de callback sea accesible públicamente. Sigue estos pasos para configurar ngrok: 

    Descarga e instala ngrok desde aquí .
    Inicia ngrok para exponer el puerto 5000:
    bash
     

     
    1
    ngrok http 5000
     
     
    Copia la URL generada por ngrok (por ejemplo, https://your-ngrok-url.ngrok-free.app) y actualiza el archivo app.py con esta URL como REDIRECT_URI.
     

Contribuciones  

¡Las contribuciones son bienvenidas! Si deseas mejorar esta aplicación, sigue estos pasos: 

    Haz un fork del repositorio.
    Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
    Realiza tus cambios y haz commit (git commit -m "Añadir nueva funcionalidad").
    Sube tus cambios (git push origin feature/nueva-funcionalidad).
    Abre un pull request.
     

Licencia  

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE  para más detalles. 
Contacto  

Si tienes preguntas o sugerencias, no dudes en contactarme: 

    Correo electrónico : freebot@gmail.com 
    GitHub : freebot
     


