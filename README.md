# Proyecto API_3B

Este proyecto es una aplicación API desarrollada con FastAPI que realiza cuatro endpoints los cuales se enfocan en la gestion de prodcutos tipo punto de venta, se manejará un sistema de alertas que se ejecuta cuando la condicion es aplicada, se generará documentación sobre la API y esetara todo montado sobre un ambiente docker simulando una arquitectura de multiprocesos, también se montara una base de datos mongodb en un contenedor externo y se realizaran consultas bajo un ORM.

## Requisitos

- Docker (Linux) o Docker Desktop (Windows y Mac) `https://www.docker.com/products/docker-desktop/`
- Python 3.9
- pip

## Instalación y Uso

1. Clona este repositorio desde GitHub `https://github.com/Garedmx/api_3b` o Descomprimir el archivo .ZIP en tu máquina local.
2. Navega al Directorio Raiz.
4. Ejecuta docker-compose para incializar los contenedores docker con: `docker-compose up -d`
5. Accede a la aplicacion en tu navegador web: `http://localhost:8000/`

## Endpoints

- GET `/api/products`: Se usa para ver la lista de productos.

- POST `/api/products`: Se usa para crear un nuevo producto con los atributos sku y name (obligatorios). Un nuevo producto siempre se crea con un stock de 100.

- PATCH `/api/inventroies/products/{sku}`: Se usa para agregar stock al producto.

- POST `/api/orders`: Para comprar productos

## Alertas

- Se creara un JOB que dispara una alerta la cual creara un LOG cuando los productos lleguen a tener un stock inferior a 10.

## Pruebas Unitarias

Para ejecutar las pruebas unitarias es necesario entrar al shell del contenedor y posteriormente ejecutar las pruebas con pytest, todo esto se puede ejecutar desde la misma terminal donde inicializo el proyecto con los siguientes comandos:
`docker exec -it api_3b-app-1 /bin/bash`
`pytest`
para salir del shell del contenedor de docker puede usar el comando `exit`

## Documentación

Se agrega in archivo llamado `documentacion_api.json` para que se facilite la importación del uso del endpoint a sistemas externos como Swagger o Postman, tambien se les recuerda que se puede acceder a la misma documentación y realizar las pruebas necesarias a los endpoints desde la url `http://localhost:8000/docs`
