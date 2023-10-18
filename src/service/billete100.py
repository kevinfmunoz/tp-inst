from billetes import ATMHandler

class BilleteCienHandler(ATMHandler):
    def dipensar(self, monto):
        if monto >= 100:
            num_bills = monto // 100
            resto = monto % 100
            print(f"se dispensaron {num_bills} $100 billetes")
            if resto > 0 and self.successor:
                self.successor.dispensar(resto)
        elif self.successor:
            self.successor.dispensar(monto)
