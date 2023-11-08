from domain.cajerohandle import CajeroHandler

class billete50service(CajeroHandler):
    def handle(self, monto):
        if monto % 50 == 0:
            return print("se han dispensado {monto}")
        else:
            return super().handle_request(monto)