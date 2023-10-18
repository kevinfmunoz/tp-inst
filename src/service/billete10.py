from billetes import ATMHandler

class BilleteDiezHandler(ATMHandler):
    def dispensar(self, monto):
        if monto >= 10:
            num_bills = monto // 10
            resto = monto % 10
            print(f"se dispensaron {num_bills} $10 billetes")
            if resto > 0 and self.successor:
                self.successor.dispensar(resto)
        elif self.successor:
            self.successor.dispensar(resto)