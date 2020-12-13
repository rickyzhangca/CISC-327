import entities

'''
This is the Repositories module enabling modifications to the databases
'''


class Repository:

    def __init__(self, filename):
        self.filename = filename
        self.readFile()

    '''
    save an entity to the database
    '''
    def save(self, new_entity):
        entity = self.findBy(new_entity.id())
        if entity:
            entity.entity = new_entity.entity
        else:
            self.collection.append(new_entity)
        
    '''
    find an entity in the database by its id
    '''
    def findBy(self, entity_id):
        for i in self.collection:
            if i.id() == entity_id:
                return i
        return None
        
    '''
    delete an entity in the database by its id
    '''
    def deleteBy(self, entity_id):
        for i in self.collection:
            if i.id() == entity_id:
                self.collection.remove(i)
                return
           
    '''
    read a database file
    '''
    def readFile(self):
        file = open(self.filename, 'r')
        self.content = file.read().split('\n')[:-1]
        file.close()

    '''
    save to a database file
    '''
    def storeFile(self):
        new_filename = self.filename
        file = open(new_filename, 'w')
        for i in self.collection:
            file.write(i.toString())
        file.close()

'''
user database
'''
class UserResourcesRepository(Repository):

    def __init__(self, filename):
        super().__init__(filename)
        self.collection = [ entities.UserResourcesEntity(i) for i in self.content ]

'''
ticket database
'''
class TicketResourcesRepository(Repository):

    def __init__(self, filename):
        super().__init__(filename)
        self.collection = [ entities.TicketResourcesEntity(i) for i in self.content ]

'''
transaction database
'''
class TransactionsRepository(Repository):

    def __init__(self, filename):
        super().__init__(filename)
        self.userCollection = []
        self.ticketCollection = []
        for i in self.content:
            if 'register' in i:
                self.userCollection.append(entities.UserTransactionsEntity(i))
            else:
                self.ticketCollection.append(entities.TicketTransactionsEntity(i))
        self.collection = []
