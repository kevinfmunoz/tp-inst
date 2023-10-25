from domain.dispenser import Dispenser

class Dollar10Dispenser(Dispenser):
    def dispense(self, amount):
        if amount >= 10:
            bills = amount // 10
            remainder = amount % 10
            print(f"Dispensing {bills} $10 bills")
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