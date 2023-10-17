from billetes import ATMHandler

class BilleteVeinteHandler(ATMHandler):
    def dispense(self, amount):
        if amount >= 20:
            num_bills = amount // 20
            remainder = amount % 20
            print(f"Dispensing {num_bills} $20 bills")
            if remainder > 0 and self.successor:
                self.successor.dispense(remainder)
        elif self.successor:
            self.successor.dispense(amount)
