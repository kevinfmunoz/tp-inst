from billete import ManejadorDinero
from service import cajero

class Billete50(ManejadorDinero):
    def manejar_dinero(self, cantidad):
        if cantidad >= 50:
            num_billetes = cantidad // 50
            if cajero.dispensar_billetes(num_billetes * 50):
                print(f"Se han dispensado {num_billetes} billetes de $50.")
            cantidad %= 50
        super().manejar_dinero(cantidad)