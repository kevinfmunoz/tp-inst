from billete import ManejadorDinero
from service import cajero

class Billete100(ManejadorDinero):
    def manejar_dinero(self, cantidad):
        if cantidad >= 100:
            num_billetes = cantidad // 100
            if cajero.dispensar_billetes(num_billetes * 100):
                print(f"Se han dispensado {num_billetes} billetes de $100.")
            cantidad %= 100
        super().manejar_dinero(cantidad)