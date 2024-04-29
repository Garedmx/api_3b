from mongoengine import connect

# Configura la conexión a la base de datos
connect(
    db="base_3b", # Nombre de la Base de Datos MongoDB
    host="mongo",  # Nombre del servicio MongoDB en Docker Compose
    port=27017,  # Puerto expuesto en el servicio MongoDB
    username="admin",
    password="Admin01"
)
