import config
import entities
import repositories


class Service:

    def __init__(self, transaction_file):
        self.userResourcesRepository = repositories.UserResourcesRepository(config.user_resources)
        self.ticketResourcesRepository = repositories.TicketResourcesRepository(config.ticket_resources)
        self.transactionsRepository = repositories.TransactionsRepository(transaction_file)

    def processTransactions(self):
        for i in self.transactionsRepository.userCollection:
            self.addUser(i)
        for i in self.transactionsRepository.ticketCollection:
            transaction_name = i.entity['transaction_name']
            if transaction_name == 'buy':
                self.buyTicket(i)
            else: # Sell or Update
                self.sellUpdateTicket(i)

    def updateDatabase(self):
        self.userResourcesRepository.storeFile()
        self.ticketResourcesRepository.storeFile()
        self.transactionsRepository.storeFile()        

    def addUser(self, transaction):
        newUser = entities.UserResourcesEntity()
        newUser.entity['user_email'] = transaction.entity['user_email']
        newUser.entity['user_name'] = transaction.entity['user_name']
        newUser.entity['user_password'] = transaction.entity['user_password']
        newUser.entity['balance'] = int(transaction.entity['balance'])
        self.userResourcesRepository.save(newUser)        

    def buyTicket(self, transaction):
        user = self.userResourcesRepository.findBy(transaction.entity['user_name'])
        ticket = self.ticketResourcesRepository.findBy(transaction.entity['ticket_name'])
        user.entity['balance'] -= ticket.entity['ticket_price'] * transaction.entity['quantity']
        ticket.entity['quantity'] -= transaction.entity['quantity']
        self.userResourcesRepository.save(user)
        self.ticketResourcesRepository.save(ticket)

    def sellUpdateTicket(self, transaction):
        ticket = entities.TicketResourcesEntity()
        ticket.entity['ticket_name'] = transaction.entity['ticket_name']
        ticket.entity['ticket_price'] = transaction.entity['ticket_price']
        ticket.entity['quantity'] = transaction.entity['quantity']
        ticket.entity['user_email'] = self.getUserEmail(transaction.entity['user_name'])
        ticket.entity['date'] = transaction.entity['date']
        self.ticketResourcesRepository.save(ticket)
    
    def getUserEmail(self, user_name):
        return self.userResourcesRepository.findBy(user_name).entity['user_email']
