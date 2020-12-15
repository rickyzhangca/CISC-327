'''
This is the Entities module assigning unique features to an entity
'''


class Entity:

    entity = None

    def id(self):
        pass

    def toString(self):
        line = ''
        for i in self.entity:
            line += str(self.entity[i]) + ', '
        return line[:-2] + '\n'

'''
user resource entity: user profile + id + can update the balance
'''
class UserResourcesEntity(Entity):

    def __init__(self, line=None):
        if line:
            record = line.split(', ')
            self.entity = {
                'user_email': record[0],
                'user_name': record[1],
                'user_password': record[2],
                'balance': int(record[3]),
            }
        else:
            self.entity = {}

    def id(self):
        return self.entity['user_name']

    def updatebalance(self, balance):
        self.entity['balance'] = balance


'''
ticket resource entity: ticket information + id + can update the quantity
'''
class TicketResourcesEntity(Entity):

    def __init__(self, line=None):
        if line:
            record = line.split(', ')
            self.entity = {
                'ticket_name': record[0],
                'ticket_price': int(record[1]),
                'quantity': int(record[2]),
                'user_email': record[3],
                'date': record[4],
            }
        else:
            self.entity = {}

    def id(self):
        return self.entity['ticket_name']
    
    def updateQuantity(self, quantity):
        self.entity['quantity'] = quantity


'''
user transaction entity: a user transaction
'''
class UserTransactionsEntity(Entity):

    def __init__(self, line=None):
        record = line.split(', ')
        self.entity = {
            'transaction_name': record[0],
            'user_name': record[1],
            'user_email': record[2],
            'user_password': record[3],
            'balance': int(record[4]),
        }


'''
ticket transaction entity: a ticket transaction
'''
class TicketTransactionsEntity(Entity):

    def __init__(self, line=None):
        record = line.split(', ')
        self.entity = {
            'transaction_name': record[0],
            'user_name': record[1],
            'ticket_name': record[2],
            'ticket_price': int(record[3]),
            'quantity': int(record[4]),
            'date': int(record[5]),
        }
