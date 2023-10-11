

class ManejadorDinero:
    def __init__(self, sucesor=None):
        self.sucesor = sucesor

    def manejar_dinero(self, cantidad):
        if self.sucesor:
            self.sucesor.manejar_dinero(cantidad)