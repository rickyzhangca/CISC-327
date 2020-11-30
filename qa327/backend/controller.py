import services


class Controller:

    def __init__(self, transaction_file):
        self.transaction_file = transaction_file
    
    def processOffice(self):
        self.userService = services.Service(self.transaction_file)
        self.userService.processTransactions()        
        self.userService.updateDatabase()
