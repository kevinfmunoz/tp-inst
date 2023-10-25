from service.dollar100dispenserservice import Dollar100Dispenser

class ATMModel:
    def __init__(self):
        self.dispenser = Dollar100Dispenser()

    def dispense_amount(self, amount):
        self.dispenser.dispense(amount)