import services


class Controller:

    def __init__(self, transaction_file):
        self.userService = services.UserService(transaction_file)
        self.ticketService = services.TicketService(transaction_file)
    
    def processOffice(self):
        self.userService.processTransactions()
        self.ticketService.processTransactions()
        self.userService.updateDatabase()
        self.ticketService.updateDatabase()