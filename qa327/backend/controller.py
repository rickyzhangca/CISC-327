import services


'''
Controls the flow of processing transactions for a given file
'''
class Controller:

    def __init__(self, transaction_file):
        self.transaction_file = transaction_file
    
    def processOffice(self):
        # perform service
        self.userService = services.Service(self.transaction_file)
        self.userService.processTransactions()    
        # udpate database    
        self.userService.updateDatabase()
