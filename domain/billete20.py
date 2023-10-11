from billete import ManejadorDinero
from service import cajero

class Billete20(ManejadorDinero):
    def manejar_dinero(self, cantidad):
        if cantidad >= 20:
            num_billetes = cantidad // 20
            if cajero.dispensar_billetes(num_billetes * 20):
                print(f"Se han dispensado {num_billetes} billetes de $20.")
            cantidad %= 20
        super().manejar_dinero(cantidad)