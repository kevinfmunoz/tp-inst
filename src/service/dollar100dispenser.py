from dispenser import Dispenser

class Dollar100Dispenser(Dispenser):
    def dispense(self, amount):
        if amount >= 100:
            bills = amount // 100
            remainder = amount % 100
            print(f"Dispensing {bills} $100 bills")
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
