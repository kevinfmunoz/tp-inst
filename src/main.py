from domain.usuariobuilder import UsuarioBuilder
from controller.atmcontroller import ATMController
from domain.atmmodel import ATMModel


if __name__ == "__main__":
    model = ATMModel()
    controller = ATMController(model)

    amount = int(input("Enter the amount to withdraw: $"))
    controller.run(amount)

def main():
    
    usuario = UsuarioBuilder().with_nombre("kevin")\
                                .with_apellido("munoz")\
                                .with_edad("19")\
                                .with_email("km6267282823@gmail.com")\
                                .with_direccion("bellocq")\
                                .build()
    
    print(usuario)

if __name__ == "__main__":
    main()