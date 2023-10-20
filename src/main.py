
from controller.atmcontroller import ATMController
from domain.atmmodel import ATMModel

if __name__ == "__main__":
    model = ATMModel()
    controller = ATMController(model)

    amount = int(input("Enter the amount to withdraw: $"))
    controller.run(amount)