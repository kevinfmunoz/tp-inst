from domain.cajero import cajero
from service.billete100service import billete100service
from service.billete50service import billete50service
from service.billete200service import billete200service


if __name__ == "__main__":
    billete100 = billete100service()
    billete200 = billete200service()
    billete50 = billete50service()

    billete100.set_next(billete50).set_next(billete200)
    
    cajero(1200)