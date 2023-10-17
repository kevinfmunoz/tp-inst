from billetes import ATMHandler

class BilleteDiezHandler(ATMHandler):
    def dispense(self, amount):
        if amount >= 10:
            num_bills = amount // 10
            print(f"Dispensing {num_bills} $10 bills")
