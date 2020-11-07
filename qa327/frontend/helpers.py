import re
import getpass
import exceptions

'''
This is the helpers module:
'''

user_info = {}
ticket_info = {}

transactions = []


'''
Helper that handle all the resorces loading and getting activities.
'''
class ResourcesHelper:

    @staticmethod
    def loadUserInfo(user_file_path):
        user_file = open(user_file_path, 'r').read().split('\n')
        for i in user_file:
            record = i.split(', ')
            user_info[record[1]] = {
                'email': record[0],
                'password': record[2],
                'balence': float(record[3]),
    }
    
    @staticmethod
    def loadTicketInfo(ticket_file_path):        
        ticket_file = open(ticket_file_path, 'r').read().split('\n')
        for i in ticket_file:
            record = i.split(', ')
            ticket_info[record[0]] = {
                'price': float(record[1]),
                'number': int(record[2]),
                'email': record[3],
    }

    @staticmethod
    def getUserInfo():
        return user_info

    
    @staticmethod
    def getTicketInfo():
        return ticket_info


'''
Helper that handle all the transactional activities, including saving and adding new transactions.
'''
class TransactionsHelper:

    @staticmethod
    def saveTransactions(location):
        transaction_file = open(location + '_transactions.csv', 'w+')
        for i in transactions:
            transaction_file.write(i)
        transaction_file.close()

    @staticmethod
    def newUserTransaction(transaction_name, user_name, user_email, user_password, balance):
        transactions.append(str(transaction_name) + ', ' + str(user_name) + ', ' + str(user_email) + ', ' + str(user_password) + ', ' + str(balance))

    @staticmethod
    def newTicketTransaction(transaction_name, user_name, ticket_name, ticket_price, quantity):
        transactions.append(str(transaction_name) + ', ' + str(user_name) + ', ' + str(ticket_name) + ', ' + str(ticket_price) + ', ' + str(quantity))


'''
Helper that handle all user inputs.
'''
class UserIOHelper:

    @staticmethod
    def acceptEmail():
        email = input('Email: ')
        if len(email) < 1:
            print('Email address cannot be empty.')
            raise exceptions.WrongFormatException()
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            print('Recieved email address:', email, 'format is incorrect.')
            raise exceptions.WrongFormatException()
        return email
    
    @staticmethod
    def acceptPassword():
        password = getpass.getpass('Password: ')
        if len(password) < 1:
            print('Password cannot be empty.')
            raise exceptions.WrongFormatException()
        if len(password) < 6:
            print('Given password is too short. Need at least 6 in length.')
            raise exceptions.WrongFormatException()
        if not any(i.isupper() for i in password):
            print('Password should contain at least one upper case character.')
            raise exceptions.WrongFormatException()
        if not any(i.islower() for i in password):
            print('Password should contain at least one lower case character.')
            raise exceptions.WrongFormatException()
        if not any(not i.isalnum() for i in password):
            print('Password should contain at least one special character.')
            raise exceptions.WrongFormatException()
        return password
    
    @staticmethod
    def acceptTicketName():
        ticket_name = input('Ticket name: ')

        if len(ticket_name) < 1 or len(ticket_name) > 60:
            raise exceptions.WrongFormatException()

        if len(ticket_name) > 1: 
            if ticket_name[0] == ' ':
                ticket_name = ticket_name[1:]
            if ticket_name[-1] == ' ':
                ticket_name = ticket_name[:-1]

        check = ticket_name.isalnum()
        if check:
            return ticket_name
        else:
            raise exceptions.WrongFormatException()
    
    @staticmethod
    def acceptTicketQuantity():
        ticket_quantity = input('Ticket quantity: ')

        if ticket_quantity.isdigit():
            ticket_quantity = int(ticket_quantity)
        else:
            raise exceptions.WrongFormatException()

        if ticket_quantity > 0 and ticket_quantity <= 100:
            return ticket_quantity
        else:
            raise exceptions.WrongTicektQuantityException()
    
    @staticmethod
    def acceptTicketPrice():
        price = input('Price: ')

        if price.isdigit():
            price = int(price)
        else:
            raise exceptions.WrongFormatException()

        if price >= 10 and price <= 100:
            return price
        else:
            raise exceptions.WrongTicektPriceException()
    
    @staticmethod
    def acceptDate():
        date = input('Date: ')

        if not date.isdigit():
            raise exceptions.WrongFormatException()

        if len(date) != 8:
            raise exceptions.WrongFormatException()
        
        if int(date[4:6]) < 1 or int(date[4:6]) > 12:
            raise exceptions.WrongDateException()
        elif int(date[6:]) < 1 or int(date[6:]) > 31:
            raise exceptions.WrongDateException()
        else:
            return date
