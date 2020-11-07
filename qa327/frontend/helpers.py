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

    current_username = 'no_username'

    @staticmethod
    def setUsername(username):
        TransactionsHelper.current_username = username

    @staticmethod
    def saveTransactions(location):
        transaction_file = open(location + '_transactions.csv', mode='a', newline=None)
        for i in transactions:
            transaction_file.write(i)
        transaction_file.close()

    @staticmethod
    def newUserTransaction(transaction_name, user_name, user_email, user_password, balance):
        transactions.append(str(transaction_name) + ', ' + str(user_name) + ', ' + str(TransactionsHelper.current_username) + ', ' + str(user_email) + ', ' + str(user_password) + ', ' + str(balance) + '\n')

    @staticmethod
    def newTicketTransaction(transaction_name, ticket_name, ticket_price, quantity):
        transactions.append(str(transaction_name) + ', ' + str(TransactionsHelper.current_username) + ', ' + str(ticket_name) + ', ' + str(ticket_price) + ', ' + str(quantity) + '\n')

'''
Helper that handle all user inputs.
'''
class UserIOHelper:
    
    @staticmethod
    def acceptEmail(unique=False):
        email = input('Email: ')
        regex = """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        import re
        if re.search(regex,email):  
            if unique:
                users = ResourcesHelper.getUserInfo()
                for u in users.items():
                    if u[1]['email'] == email:
                        raise exceptions.WrongFormatException('Email')
            return email
        else:  
            raise exceptions.WrongFormatException('Email')
    
    @staticmethod
    def acceptPassword():
        password = getpass.getpass('Password: ')
        if len(password) < 1:
            print('Password cannot be empty.')
            raise exceptions.WrongFormatException('Password')
        if len(password) < 6:
            print('Given password is too short. Need at least 6 in length.')
            raise exceptions.WrongFormatException('Password')
        if not any(i.isupper() for i in password):
            print('Password should contain at least one upper case character.')
            raise exceptions.WrongFormatException('Password')
        if not any(i.islower() for i in password):
            print('Password should contain at least one lower case character.')
            raise exceptions.WrongFormatException('Password')
        if not any(not i.isalnum() for i in password):
            print('Password should contain at least one special character.')
            raise exceptions.WrongFormatException('Password')
        return password
    
    @staticmethod
    def acceptPassword2(password):
        password2 = getpass.getpass('Confirm password: ')
        return password2 == password
    
    @staticmethod
    def acceptTicketName():
        ticket_name = input('Ticket name: ')

        if len(ticket_name) < 1 or len(ticket_name) > 60:
            raise exceptions.WrongFormatException('Ticket name')

        if len(ticket_name) > 1: 
            if ticket_name[0] == ' ':
                ticket_name = ticket_name[1:]
            if ticket_name[-1] == ' ':
                ticket_name = ticket_name[:-1]

        check = ticket_name.isalnum()
        if check:
            return ticket_name
        else:
            raise exceptions.WrongFormatException('Ticket name')
    
    @staticmethod
    def acceptTicketQuantity():
        ticket_quantity = input('Ticket quantity: ')

        if ticket_quantity.isdigit():
            ticket_quantity = int(ticket_quantity)
        else:
            raise exceptions.WrongFormatException('Ticket quantity')

        if ticket_quantity > 0 and ticket_quantity <= 100:
            return ticket_quantity
        else:
            raise exceptions.WrongTicketQuantityException()
    
    @staticmethod
    def acceptTicketPrice():
        price = input('Price: ')

        if price.isdigit():
            price = int(price)
        else:
            raise exceptions.WrongFormatException('Ticket price')

        if price >= 10 and price <= 100:
            return price
        else:
            raise exceptions.WrongTicketPriceException()
    
    @staticmethod
    def acceptDate():
        date = input('Date: ')

        if not date.isdigit():
            raise exceptions.WrongFormatException('Date')

        if len(date) != 8:
            raise exceptions.WrongFormatException('Date')
        
        if int(date[4:6]) < 1 or int(date[4:6]) > 12:
            raise exceptions.WrongFormatException('Date')
        elif int(date[6:]) < 1 or int(date[6:]) > 31:
            raise exceptions.WrongFormatException('Date')
        else:
            return date

    @staticmethod
    def acceptUsername():
        username = input('Username: ')

        if len(username) <= 2 or len(username) >= 20:
            raise exceptions.WrongFormatException()

        if len(username) > 1: 
            if username[0] == ' ':
                username = username[1:]
            if username[-1] == ' ':
                username = username[:-1]

        check = username.isalnum()
        if check:
            return username
        else:
            raise exceptions.WrongFormatException()
