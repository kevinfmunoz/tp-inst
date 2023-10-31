from domain.cajerohandle import CajeroHandler

class billete200service(CajeroHandler):
    def handle(self, monto):
        if monto % 200 == 0:
            return print("se han dispensado {monto}")
        else:
            return super().handle_request(monto)