import config
import controller


def main():

    # process Kingston transactions
    kingstonController = controller.Controller(config.kingston_transaction)
    kingstonController.processOffice()

    # process Toronto transactions
    torontoController = controller.Controller(config.toronto_transaction)
    torontoController.processOffice()

    # process Montreal transactions
    montrealController = controller.Controller(config.montreal_transaction)
    montrealController.processOffice()