from domain.cajerohandle import CajeroHandler

class billete100service(CajeroHandler):
    def handle(self, monto):
        if monto % 100 == 0:
            return print("se han dispensado {monto}")
        else:
            return super().handle_request(monto)