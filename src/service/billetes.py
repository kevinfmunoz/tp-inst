from abc import ABC

class ATMHandler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    def dispense(self, amount):
        pass