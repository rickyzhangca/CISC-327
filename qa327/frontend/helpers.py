import re
import getpass
import exceptions

user_info = {}
ticket_info = {}

location = None

transactions = []

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


class TransactionsHelper:

    @staticmethod
    def saveTransactions(location):
        transaction_file = open(location + '_transactions.csv', 'w+')
        for i in transactions:
            transaction_file.write(i)
        transaction_file.close()

    @staticmethod
    def newUserTransaction(transaction_name, user_name, user_email, user_password, balance):
        transactions.append(transaction_name + ', ' + user_name + ', ' + user_email + ', ' + user_password + ', ' + balance)

    @staticmethod
    def newTicketTransaction(transaction_name, user_name, ticket_name, ticket_price, quantity):
        transactions.append(transaction_name + ', ' + user_name + ', ' + ticket_name + ', ' + ticket_price + ', ' + quantity)

class UserIOHelper:

    @staticmethod
    def acceptEmail():
        email = input('Email: ')
        if len(email) < 1:
            print('Email address cannot be empty.')
            raise exceptions.FormatingException()
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            print('Recieved email address:', email, 'format is incorrect.')
            raise exceptions.FormatingException()
        return email
    
    @staticmethod
    def acceptPassword():
        password = getpass.getpass('Password: ')
        if len(password) < 1:
            print('Password cannot be empty.')
            raise exceptions.FormatingException()
        if len(password) < 6:
            print('Given password is too short. Need at least 6 in length.')
            raise exceptions.FormatingException()
        if not any(i.isupper() for i in password):
            print('Password should contain at least one upper case character.')
            raise exceptions.FormatingException()
        if not any(i.islower() for i in password):
            print('Password should contain at least one lower case character.')
            raise exceptions.FormatingException()
        if not any(not i.isalnum() for i in password):
            print('Password should contain at least one special character.')
            raise exceptions.FormatingException()
        return password