from dispenser import Dispenser

class Dollar50Dispenser(Dispenser):
    def dispense(self, amount):
        if amount >= 50:
            bills = amount // 50
            remainder = amount % 50
            print(f"Dispensing {bills} $50 bills")
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