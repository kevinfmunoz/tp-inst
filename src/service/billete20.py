from billetes import ATMHandler

class BilleteVeinteHandler(ATMHandler):
    def dispensar(self, monto):
        if monto >= 20:
            num_bills = monto // 20
            resto = monto % 20
            print(f"se dispensaron {num_bills} $20 billetes")
            if resto > 0 and self.successor:
                self.successor.dispensar(resto)
        elif self.successor:
            self.successor.dispensar(resto)
