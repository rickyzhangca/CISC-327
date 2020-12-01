import entities

'''
This is the Repositories module
'''


class Repository:

    def __init__(self, filename):
        self.filename = filename
        self.readFile()

    def save(self, new_entity):
        entity = self.findBy(new_entity.id())
        if entity:
            entity.entity = new_entity.entity
        else:
            self.collection.append(new_entity)
        
    def findBy(self, entity_id):
        for i in self.collection:
            if i.id() == entity_id:
                return i
        return None

    def deleteBy(self, entity_id):
        for i in self.collection:
            if i.id() == entity_id:
                self.collection.remove(i)
                return
    
    def readFile(self):
        file = open(self.filename, 'r')
        self.content = file.read().split('\n')[:-1]
        file.close()

    def storeFile(self):
        new_filename = self.filename
        if self.collection:
            new_filename = new_filename.replace('data/', 'data/updated_')
        file = open(new_filename, 'w')
        for i in self.collection:
            file.write(i.toString())
        file.close()


class UserResourcesRepository(Repository):

    def __init__(self, filename):
        super().__init__(filename)
        self.collection = [ entities.UserResourcesEntity(i) for i in self.content ]


class TicketResourcesRepository(Repository):

    def __init__(self, filename):
        super().__init__(filename)
        self.collection = [ entities.TicketResourcesEntity(i) for i in self.content ]


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
