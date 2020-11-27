import entities

'''
This is the Repositories module
'''


class Repository:

    def __init__(self, filename):
        self.filename = filename
        self.readFile()

    def save(self, new_entity):
        entity = findBy(new_entity.entity.id)
        if entity:
            entity.entity = new_entity.entity
        else:
            self.collection.append(new_entity)
        
    def findBy(self, entity_id):
        for i in self.collection:
            if i.id() == entity_id:
                return i.entity
        return None

    def deleteBy(self, entity_id):
        for i in self.collection:
            if i.id() == entity_id:
                self.collection.remove(i)
                return
    
    def readFile(self):
        file = open(filename, 'r')
        self.content = file.read().split('\n')
        file.close()

    def storeFile(self):
        file = open(filename, 'w+')
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
        self.UserCollection = []
        self.TicketCollection = []
        for i in self.content:
            if 'register' in i:
                self.UserCollection.append(entities.UserTransactionsEntity(i))
            else:
                self.TicketCollection.append(entities.TicketTransactionsEntity(i))
        self.collection = []
