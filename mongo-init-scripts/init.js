// Crear una base de datos llamada "base_3b"
db = db.getSiblingDB('base_3b');

// Crear un usuario administrador con la contraseña "Admin01"
db.createUser({
    user: 'admin',
    pwd: 'Admin01',
    roles: [{ role: 'root', db: 'admin' }]
});
