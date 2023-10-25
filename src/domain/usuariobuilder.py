from domain.user import Usuario

class UsuarioBuilder:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UsuarioBuilder, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.edad = 0
        self.email = ""
        self.direccion = ""

    def with_nombre(self, nombre):
        self.nombre = nombre
        return self

    def with_apellido(self, apellido):
        self.apellido = apellido
        return self

    def with_edad(self, edad):
        self.edad = edad
        return self

    def with_email(self, email):
        self.email = email
        return self

    def with_direccion(self, direccion):
        self.direccion = direccion
        return self

    def build(self):
        return Usuario(self.nombre, self.apellido, self.edad, self.email, self.direccion)
