from service.billete10 import BilleteCienHandler
from service.billete50 import BilleteCincuentaHandler
from service.billete20 import BilleteVeinteHandler
from service.billete10 import BilleteDiezHandler

if __name__ == "__main__":
    cien_handler = BilleteCienHandler()
    cincuenta_handler = BilleteCincuentaHandler()
    veinte_handler = BilleteVeinteHandler()
    diez_handler = BilleteDiezHandler()

    amount_to_withdraw = 370
    cien_handler.dispense(amount_to_withdraw)