from mongoengine import connect

def conectar():
    # Configura la conexión a la base de datos
    connect(
        db="punto_venta", # Nombre de la Base de Datos MongoDB
        host="mongo",  # Nombre del servicio MongoDB en Docker Compose
        port=27017,  # Puerto expuesto en el servicio MongoDB
)
