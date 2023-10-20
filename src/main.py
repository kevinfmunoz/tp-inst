from controller.usuariobuilder import UsuarioBuilder
from controller.atmcontroller import ATMController
from domain.atmmodel import ATMModel

if __name__ == "__main__":
    model = ATMModel()
    controller = ATMController(model)

    amount = int(input("Enter the amount to withdraw: $"))
    controller.run(amount)

def main():
    usuario_builder = UsuarioBuilder()
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    email = input("Email: ")
    direccion = input("Dirección: ")
    
    usuario = usuario_builder \
        .with_nombre(nombre) \
        .with_apellido(apellido) \
        .with_edad(edad) \
        .with_email(email) \
        .with_direccion(direccion) \
        .build()
    
    print(usuario)

if __name__ == "__main__":
    main()