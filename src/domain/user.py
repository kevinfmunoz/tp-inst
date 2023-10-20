class Usuario:
    def __init__(self, nombre, apellido, edad, email, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email
        self.direccion = direccion

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido}, Edad: {self.edad}, Email: {self.email}, Dirección: {self.direccion}"
