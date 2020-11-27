import config
import controller


def main():

    kingstonController = controller.Controller(config.kingston_transaction)
    kingstonController.processOffice()

    torontoController = controller.Controller(config.toronto_transaction)
    torontoController.processOffice()

    montrealController = controller.Controller(config.montreal_transaction)
    montrealController.processOffice()