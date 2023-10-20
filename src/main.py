from domain.usuariobuilder import UsuarioBuilder
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
    
    usuario = usuariocontroler.create_usuario()
    
    print(usuario)

if __name__ == "__main__":
    main()