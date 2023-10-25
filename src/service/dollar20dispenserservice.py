from domain.dispenser import Dispenser

class Dollar20Dispenser(Dispenser):
    def dispense(self, amount):
        if amount >= 20:
            bills = amount // 20
            remainder = amount % 20
            print(f"Dispensing {bills} $20 bills")
            if remainder > 0:
                if self.next_dispenser is not None:
                    self.next_dispenser.dispense(remainder)
                else:
                    print(f"Can't dispense {remainder} amount")
        else:
            if self.next_dispenser is not None:
                self.next_dispenser.dispense(amount)
            else:
                print(f"Can't dispense {amount} amount")