import services


class Controller:

    def __init__(self, transaction_file):
        self.transaction_file = transaction_file
    
    def processOffice(self):
        self.userService = services.UserService(self.transaction_file)
        self.userService.processTransactions()        
        self.userService.updateDatabase()
        
        self.ticketService = services.TicketService(self.transaction_file)        
        self.ticketService.processTransactions()
        self.ticketService.updateDatabase()