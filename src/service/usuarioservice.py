from domain.usuariobuilder import UsuarioBuilder

class Usuarioservice():

    def create_user():
        UsuarioBuilder \
        .with_nombre(nombre) \
        .with_apellido(apellido) \
        .with_edad(edad) \
        .with_email(email) \
        .with_direccion(direccion) \
        .build()