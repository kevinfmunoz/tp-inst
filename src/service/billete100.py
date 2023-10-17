from billetes import ATMHandler

class BilleteCienHandler(ATMHandler):
    def dispense(self, amount):
        if amount >= 100:
            num_bills = amount // 100
            remainder = amount % 100
            print(f"Dispensing {num_bills} $100 bills")
            if remainder > 0 and self.successor:
                self.successor.dispense(remainder)
        elif self.successor:
            self.successor.dispense(amount)
