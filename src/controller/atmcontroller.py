class ATMController:
    def __init__(self, model):
        self.model = model

    def run(self, amount):
        self.model.dispense_amount(amount)
