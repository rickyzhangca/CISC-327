import re
import getpass
import exceptions
import datetime as dt
import os

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
                'balence': int(record[3]),
            }
    
    @staticmethod
    def loadTicketInfo(ticket_file_path):        
        ticket_file = open(ticket_file_path, 'r').read().split('\n')
        for i in ticket_file:
            record = i.split(', ')
            ticket_info[record[0]] = {
                'price': int(record[1]),
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
        # update translate information
        transaction_file = open(location + '_transactions.csv', mode='a+', newline=None)
        for i in transactions:
            transaction_file.write(i)
        transaction_file.close()

    @staticmethod
    def newUserTransaction(transaction_name, user_name, user_email, user_password, balance):
        # the new user in string list add on
        transactions.append(str(transaction_name) + ', ' + str(user_name) + ', ' + str(user_email) + ', ' + str(user_password) + ', ' + str(balance) + '\n')

    @staticmethod
    def newTicketTransaction(transaction_name, user_name, ticket_name, ticket_price, quantity):
        # the new transaction uodate string list add on
        transactions.append(str(transaction_name) + ', ' + str(user_name) + ', ' + str(ticket_name) + ', ' + str(ticket_price) + ', ' + str(quantity) + '\n')


'''
Helper that handle all user inputs.
'''
class UserIOHelper:
    '''
        check email if it is valid
        '''
    @staticmethod
    def acceptEmail():
        email = input('Email: ')
        regex = """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        if not re.search(regex,email):
            raise exceptions.WrongFormatException('Email should be in a form of xxxx@xxxx.xxx')
        return email
    
    @staticmethod
    def acceptPassword():
        #minimum 6 characters long, at least one upper case, at least one lower case, at least one special character
        password = getpass.getpass('Password: ')
        if len(password) < 1:
            raise exceptions.WrongFormatException('Password cannot be empty')
        if len(password) < 6:
            raise exceptions.WrongFormatException('Given password is too short. Need at least 6 in length')
        if not any(i.isupper() for i in password):
            raise exceptions.WrongFormatException('Password should contain at least one upper case character')
        if not any(i.islower() for i in password):
            raise exceptions.WrongFormatException('Password should contain at least one lower case character')
        if not any(not i.isalnum() for i in password):
            raise exceptions.WrongFormatException('Password should contain at least one special character')
        return password
    
    @staticmethod
    def acceptPassword2():
        password2 = getpass.getpass('Confirm password: ')
        return password2
    
    @staticmethod
    def acceptTicketName():
        #name of the ticket is no longer than 60 characters
        #The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.
        ticket_name = input('Ticket name: ')
        if len(ticket_name) < 1:
            raise exceptions.WrongFormatException('The name of the ticket cannot be empty')
        if len(ticket_name) > 60:
            raise exceptions.WrongFormatException('The name of the ticket is no longer than 60 characters')
        if ticket_name[0] == ' ' or ticket_name[-1] == ' ':
            raise exceptions.WrongFormatException('Space not on the first or the last character')
        if not all(x.isalnum() or x.isspace() for x in ticket_name):
            raise exceptions.WrongFormatException('The name of the ticket has to be alphanumeric and space only')
        return ticket_name

    @staticmethod
    def acceptTicketQuantity():
        #The quantity of the tickets has to be more than 0, and less than or equal to 100.
        ticket_quantity = input('Ticket quantity: ')
        if len(ticket_quantity) < 1 or not ticket_quantity.isdigit():
            raise exceptions.WrongFormatException('Ticket quantity should be number')
        ticket_quantity = int(ticket_quantity)
        if ticket_quantity < 1 or ticket_quantity > 100:
            raise exceptions.WrongTicketQuantityException('The quantity of the tickets has to be more than 0, and less than or equal to 100.')
        return ticket_quantity

    @staticmethod
    def acceptTicketPrice():
        #Price has to be of range [10, 100]
        price = input('Price: ')
        if len(price) < 1 or not price.isdigit():
            raise exceptions.WrongFormatException('Ticket price should be number')
        price = int(price)
        if price < 1 or price > 100:
            raise exceptions.WrongTicketQuantityException('Price has to be of range [10, 100].')
        return price
    
    @staticmethod
    def acceptDate():
        date = input('Date: ')
        if not date.isdigit():
            raise exceptions.WrongFormatException('Date should be numebr')
        if len(date) != 8:
            raise exceptions.WrongFormatException('Date must be given in the format YYYYMMDD (e.g. 20200901)')        
        if int(date[4:6]) < 1 or int(date[4:6]) > 12:
            raise exceptions.WrongFormatException('month is incorrect')
        elif int(date[6:]) < 1 or int(date[6:]) > 31:
            raise exceptions.WrongFormatException('Day is incorrect')
        else:
            return date

    @staticmethod
    def acceptUserName():
        userName = input('User name: ')
        if len(userName) <= 2 or len(userName) >= 20:
            raise exceptions.WrongFormatException()
        if userName[0] == ' ' or userName[-1] == ' ':
            raise exceptions.WrongFormatException('Space not on the first or the last character')
        if not userName.isalnum():
            raise exceptions.WrongFormatException('User name should not contains special characters')
        return userName
