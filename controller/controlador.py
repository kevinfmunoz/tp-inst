from service import cajero
from domain import billete20, billete50, billete100, billete

class ControladorCajero:
    def __init__(self):
        self.chain = None

    def establecer_chain(self, chain):
        self.chain = chain

    def dispensar_dinero(self, cantidad):
        if self.chain:
            self.chain.manejar_dinero(cantidad)
