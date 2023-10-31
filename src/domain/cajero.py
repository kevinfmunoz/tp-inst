from controller.cajerocontroller import AtmHandler

class cajero(AtmHandler):
    def cajero(handler: AtmHandler):
        for monto in [100, 200, 50]:
            print("cuanto desea retirar {monto}?")
            resultado = handler.handle(monto)
            if resultado:
                print("{resultado}")
            else:
                print("el monto {monto} no se pudo retirar")
