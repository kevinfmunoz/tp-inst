from billetes import ATMHandler

class BilleteCincuentaHandler(ATMHandler):
    def dispense(self, amount):
        if amount >= 50:
            num_bills = amount // 50
            remainder = amount % 50
            print(f"Dispensing {num_bills} $50 bills")
            if remainder > 0 and self.successor:
                self.successor.dispense(remainder)
        elif self.successor:
            self.successor.dispense(amount)