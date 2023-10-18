from billetes import ATMHandler

class BilleteCincuentaHandler(ATMHandler):
    def dispensar(self, monto):
        if monto >= 50:
            num_bills = monto // 50
            resto = monto % 50
            print(f"se dispensaron {num_bills} $50 billetes")
            if resto > 0 and self.successor:
                self.successor.dispensar(resto)
        elif self.successor:
            self.successor.dispensar(resto)