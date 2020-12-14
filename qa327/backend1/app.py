import sys
from datetime import datetime
import config
import controller


def main():    
    sys.path.append('qa327/backend')
    print(datetime.now(), 'INFO --- Starting backend application')
    print()
    # location of the frontend hosting
    if len(sys.argv) > 1:
        transaction_file = sys.argv[-1]
        transaction_controller = controller.Controller(transaction_file)
        transaction_controller.processOffice()
    else:
        # process Kingston transactions
        kingston_controller = controller.Controller(config.kingston_transaction)
        kingston_controller.processOffice()

        # process Toronto transactions
        toronto_controller = controller.Controller(config.toronto_transaction)
        toronto_controller.processOffice()

        # process Montreal transactions
        montreal_controller = controller.Controller(config.montreal_transaction)
        montreal_controller.processOffice()
    print(datetime.now(), 'INFO --- Ending backend application')