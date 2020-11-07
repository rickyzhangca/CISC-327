import getpass
import exceptions
import datetime as dt

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
                'name': str(record[0]),
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
        transaction_file = open(location + '_transactions.csv', mode='a', newline=None)
        for i in transactions:
            transaction_file.write(i)
        transaction_file.close()

    @staticmethod
    def newUserTransaction(transaction_name, user_name, user_email, user_password, balance):
        transactions.append(str(transaction_name) + ', ' + str(user_name) + ', ' + str(user_email) + ', ' + str(user_password) + ', ' + str(balance) + '\n')

    @staticmethod
    def newTicketTransaction(transaction_name, user_name, ticket_name, ticket_price, quantity):
        transactions.append(str(transaction_name) + ', ' + str(user_name) + ', ' + str(ticket_name) + ', ' + str(ticket_price) + ', ' + str(quantity) + '\n')

    def newUserTransactionAfterBuy(transaction_name, user_name, user_email, user_password, balance):
        transactions.append(str(transaction_name) + ', ' + str(user_name) + ', ' + str(user_email) + ', ' + str(user_password) + ', ' + str(balance) + '\n')

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
            raise exceptions.WrongFormatException('The name of the ticket is no longer than 60 characters')

        if len(ticket_name) > 1: 
            if ticket_name[0] == ' ' or ticket_name[-1] == ' ':
                raise exceptions.WrongFormatException('Space not on the first or the last character')

        check = all(x.isalnum() or x.isspace() for x in ticket_name)
        if check:
            return ticket_name
        else:
            raise exceptions.WrongFormatException('The name of the ticket has to be alphanumeric and space only')
    
    @staticmethod
    def checkTicketName():
        flag = True
        while flag:
            name = input("Please enter the tickets' name you'd like to sell: ")
            if (not name == ""):
                # check if ticket name is alphanumeric and space only, check if space not the first or the last character.
                if all(x.isalnum() or x.isspace() for x in name):
                    # check if the name of the ticket is no longer than 60 characters
                    if (not name[0].isspace() and not name[-1].isspace()):
                        if (len(name) <= 60):
                            flag = False
                            return name
                        else:
                            print("The ticket's name should less than 60 charaters")
                    else:
                        print("Space not allow in first or last charater in ticket's name")
                else:
                    print("The name of the ticket has to be alphanumeric-only,")
    

    # check if the ticketName valid
    def buyTicketName(username):
        flag = True
        while flag:
            name = input("Please enter the tickets' name you'd like to buy.: ")
            if (not name == ""):
                # check if ticket name is alphanumeric and space only, check if space not the first or the last character.
                if all(x.isalnum() or x.isspace() for x in name):
                    # check if the name of the ticket is no longer than 60 characters
                    if (not name[0].isspace() and not name[-1].isspace()):
                        if (len(name) <= 60):
                            for i in ResourcesHelper.getTicketInfo():
                                # print(helpers.ResourcesHelper.getTicketInfo()[i]['name'])
                                if ResourcesHelper.getTicketInfo()[i]['name'] == name:
                                    # check the available quantity of this ticket
                                    quantity = ResourcesHelper.getTicketInfo()[i]['number']
                                    price = ResourcesHelper.getTicketInfo()[i]['price']
                                    print("available ticket quantity for %s is " % name + str(quantity))
                                    return name, quantity, price

                            
                            print("sorry, we do not have %s yet" %name)
                        else:
                            print("The ticket's name should less than 60 charaters")
                    else:
                        print("Space not allow in first or last charater in ticket's name")
                else:
                    print("The name of the ticket has to be alphanumeric-only")


    @staticmethod
    def acceptTicketQuantity():
        ticket_quantity = input('Ticket quantity: ')

        if len(ticket_quantity) > 0 and ticket_quantity.isdigit():
            ticket_quantity = int(ticket_quantity)
        else:
            raise exceptions.WrongFormatException('Ticket quantity should be number')

        if ticket_quantity > 0 and ticket_quantity <= 100:
            flag = True
            return ticket_quantity
        else:
            raise exceptions.WrongTicketQuantityException('The quantity of the tickets has to be more than 0, and less than or equal to 100')
    
    @staticmethod
    def checkTicketQuantity(quantity):
        flag = True
        while flag:
            ticket_quantity = input('Ticket quantity: ')

            if len(ticket_quantity) > 0 and ticket_quantity.isdigit():
                ticket_quantity = int(ticket_quantity)

                if ticket_quantity > 0 and ticket_quantity <= int(quantity):
                    flag = False
                    return ticket_quantity
                else:
                    print('The quantity of the tickets has to be more than 0, and less than or equal to %s'&quantity)
            
            else:
                print('Ticket quantity should be number')

    @staticmethod
    def acceptTicketPrice():
        price = input('Price: ')

        if len(price) > 0 and price.isdigit():
            price = int(price)
        else:
            raise exceptions.WrongFormatException('Ticket price should be number')

        if price >= 10 and price <= 100:
            flag = True
            return price
        else:
            raise exceptions.WrongTicketPriceException('Price has to be of range [10, 100]')

    @staticmethod
    def checkTicketPrice():
        flag = True
        while flag:
            price = input('Price: ')

            if len(price) > 0 and price.isdigit():
                price = int(price)

                if price >= 10 and price <= 100:
                    flag = False
                    return price
                else:
                    print('Price has to be of range [10, 100]')
            else:
                print('Ticket price should be number')

    @staticmethod
    # The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)
    def balanceAfterbuy(price, quantities, balance):
        ticket_price = 1.05 * ((1.35 * float(price)) * float(quantities))
        balance_now = float(balance) - ticket_price
        if balance_now >= 0:
            #print("valid")
            print("Total price: ", ticket_price)
            return balance_now
        else:
            print("Balance not enough, still need: $", str(balance_now))
    
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
    def checkDate():
        flag = True
        while flag:
            date = input("Date of Ticket YYYYMMDD (e.g. 20200202): ")
            if (not date == "" and date.isnumeric()):
                # Date must be given in the format YYYYMMDD (e.g. 20200901)
                if (len(date) == 8):
                    if int(date[4:6]) > 0 and int(date[4:6]) < 13:
                        if int(date[6:]) > 0 and int(date[6:]) < 32:
                            day = dt.datetime.strptime(date, '%Y%m%d').date()
                            # check if the valid date
                            if day >= dt.datetime.today().date():
                                return date

                    else:
                        print("Unavailable date")

                else:
                    print("Date must be given in the format YYYYMMDD (e.g. 20200901)")

            else:
                print("Date must be given in the format YYYYMMDD (e.g. 20200901)")



    @staticmethod
    def acceptUsername():
        username = input('Username: ')

        if len(username) <= 2 or len(username) >= 20:
            raise exceptions.WrongFormatException()

        if username[0] == ' ' or username[-1] == ' ':
            raise exceptions.WrongFormatException('Space not on the first or the last character')

        check = username.isalnum()
        if check:
            return username
        else:
            raise exceptions.WrongFormatException()
