from datetime import datetime
import services


'''
Controls the flow of processing transactions for a given file
'''
class Controller:

    def __init__(self, transaction_file):
        self.transaction_file = transaction_file
    
    def processOffice(self):        
        print(datetime.now(), 'INFO --- Start processing \''+ self.transaction_file + '\'')
        # perform service
        self.service = services.Service(self.transaction_file)
        self.service.processTransactions()    
        # udpate database
        self.service.updateDatabase()
        print(datetime.now(), 'INFO --- Done processing \''+ self.transaction_file + '\'')
        print()
