from domain import billete, billete100, billete20, billete50
from controller import controlador

class CajeroAutomatico:
    def __init__(self):
        self.saldo = 10000  

    def dispensar_billetes(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            return True
        return False