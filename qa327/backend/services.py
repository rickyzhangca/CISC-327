import config
import entities
import repositories


class service:

    def __init__(self, transaction_file):
        self.userResourcesRepository = repositories.UserResourcesRepository(config.user_resources)
        self.ticketResourcesRepository = repositories.TicketResourcesRepository(config.ticket_resources)
        self.transactionsRepository = repositories.TransactionsRepository(transaction_file)

    def processTransactions(self):
        pass

    def updateDatabase(self):
        self.userResourcesRepository.storeFile()
        self.ticketResourcesRepository.storeFile()
        self.transactionsRepository.storeFile()

class UserService(Service):

    def __init__(self, transaction_file):
        super.__init__(transaction_file)

    def processTransactions(self):
        for i in self.transactionsRepository.userCollection:
            self.addUser(i)

    def addUser(self, transaction):
        newUser = entities.UserResourcesEntity()
        newUser.entity['user_email'] = transaction['user_email']
        newUser.entity['user_name'] = transaction['user_name']
        newUser.entity['user_password'] = transaction['user_password']
        newUser.entity['balence'] = int(transaction['balence'])
        self.userResourcesRepository.save(newUser)

class TicketService(Service):

    def __init__(self, transaction_file):
        super.__init__(transaction_file)

    def processTransactions(self):
        for i in self.transactionsRepository.ticketCollection:
            transaction_name = i.entity['transaction_name']
            if transaction_name == 'buy':
                self.buyTicket(i)
            else: # Sell or Update
                self.sellUpdateTicket(i)

    def buyTicket(self, transaction):
        user = self.userResourcesRepository.findBy(transaction['user_name'])
        ticket = self.ticketResourcesRepository.findBy(transaction['ticket_name'])
        user.entity['balence'] -= ticket.entity['ticket_price'] * transaction['quantity']
        ticket.entity['quantity'] -= transaction['quantity']
        self.userResourcesRepository.save(user)
        self.ticketResourcesRepository.save(ticket)

    def sellUpdateTicket(self, transaction):
        ticket = entities.TicketResourcesEntity()
        ticket.entity['ticket_price'] = transaction['ticket_price']
        ticket.entity['quantity'] = transaction['quantity']
        ticket.entity['user_email'] = self.getUserEmail(transaction['user_name'])
        ticket.entity['date'] = transaction['date']
        self.ticketResourcesRepository.save(ticket)
    
    def getUserEmail(self, user_name):
        return self.userResourcesRepository.findBy(user_name)['user_email']
