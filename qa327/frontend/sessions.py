import helpers
import exceptions
import datetime as dt

'''
This is the sessions module:
'''

'''
Base class with the basic structure of all frontend sessions.
'''
class Session:

    # username is None when no one logged in.
    def __init__(self, username = None):
        self.username = username

    # return with the object of the next session.
    def routing(self):
        return self

    # functionality of the current session.
    def operate(self):
        pass


'''
Base class for sessions that required login.
'''
class LoggedInSession(Session):

    # raise exceptions if user have not logged in.
    def __init__(self, username):
        super().__init__(username)   
        if not username:
            print('Invaild command, user must be logged in first')
            raise exceptions.CannotAccessPageException()
    
    def routing(self):
        return LandingSession(self.username)
        
    def getBalence(self):
        pass

    def getMenu(self):
        return 'buy, sell, update, and logout'


'''
Base class for sessions that does not required login.
'''
class UnloggedInSession(Session):

    # raise exceptions if user have logged in.
    def __init__(self, username): 
        super().__init__() 
        if username:
            print('Invaild command, user must be logged out first')
            raise exceptions.CannotAccessPageException()

    def routing(self):
        return LandingSession()

    def getMenu(self):
        return 'login, register, and exits'


'''
Landing page that displays usermenu and balence.
'''
class LandingSession(Session):

    def __init__(self, username = None):
        super().__init__(username)
    
    # go to corresponding sessions.
    def routing(self):
        try:
            if self.command == 'login':
                new_session = LoginSession(self.username)
            elif self.command == 'register':
                new_session = RegisterSession(self.username)
            elif self.command == 'buy':
                new_session = BuySession(self.username)
            elif self.command == 'sell':
                new_session = SellSession(self.username)
            elif self.command == 'update':
                new_session = UpdateSession(self.username)
            elif self.command == 'logout':
                new_session = LogoutSession(self.username)
            elif self.command == 'exits':
                new_session = ExitSession(self.username)
            else:
                print('Command undefind.')
                new_session = self
        except exceptions.CannotAccessPageException:
            new_session = self
        return new_session
    
    def operate(self):
        print('\nLanding Screen...')        
        self.showBalence()
        self.displayMenu()
        self.getUserCommand()
    
    # display user menu depend on whether the user logged in.
    def displayMenu(self):
        print('Menu options - ', end = '')
        if self.username:
            print(LoggedInSession.getMenu(self))
        else:
            print(UnloggedInSession.getMenu(self))

    def showBalence(self):
        if self.username:
            print('\nHi', self.username + '!')
            print('Your balance is: $' + str(helpers.ResourcesHelper.getUserInfo()[self.username]['balence']) + '.\n')

    def getUserCommand(self):
        self.command = input('Your command: ')


'''
session that guide the user's login process.
'''
class LoginSession(UnloggedInSession):

    def __init__(self, username):
        super().__init__(username)
        self.username = None
    
    def routing(self):
        return LandingSession(self.username)
    
    def operate(self):
        print('\nLog in session starts...')
        try:
            email = helpers.UserIOHelper.acceptEmail()
            password = helpers.UserIOHelper.acceptPassword()            
            self.authorize(email, password)
        except exceptions.WrongFormatException:            
            print('Login failed, ending session...')
    
    # authorize email and password the user inputed. Setup username. 
    def authorize(self, email, password):
        for i in helpers.ResourcesHelper.getUserInfo():
            if helpers.ResourcesHelper.getUserInfo()[i]['email'] == email and helpers.ResourcesHelper.getUserInfo()[i]['password'] == password:
                print('Account logged in!')
                self.username = i
                return
        print('Email or password incorrect.')


class RegisterSession(UnloggedInSession):

    def __init__(self, username):
        super().__init__(username)
        self.username = None
    
    def operate(self):
        user_email = helpers.UserIOHelper.acceptEmail(unique=True)
        user_name = helpers.UserIOHelper.acceptUsername()
        user_password = helpers.UserIOHelper.acceptPassword()
        if not helpers.UserIOHelper.acceptPassword2(user_password):
            raise exceptions.WrongFormatException('Password 2')

        helpers.TransactionsHelper.newUserTransaction("register", user_name, user_email, user_password, 3000)
    
    '''def authorize(self, username, password):
        self.username = username'''

class SellSession(LoggedInSession):

    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        print('\nSellSession...')


class BuySession(LoggedInSession):

    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        print('\nBuySession...')


class UpdateSession(LoggedInSession):

    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        ticket_name = helpers.UserIOHelper.acceptTicketName()
        ticket_quantity = helpers.UserIOHelper.acceptTicketQuantity()
        ticket_price = helpers.UserIOHelper.acceptTicketPrice()
        date = helpers.UserIOHelper.acceptDate()
        helpers.TransactionsHelper.newTicketTransaction("update", self.username, ticket_name, ticket_price, ticket_quantity)


'''
User logout.
'''
class LogoutSession(LoggedInSession):

    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        print('\nLogout Successfully!')

    def routing(self):
        return LandingSession(None)


'''
Exiting the program.
'''
class ExitSession(UnloggedInSession):

    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        print('\nSaving transactions & exit...')

    def routing(self):
        return None

class SellSession(LoggedInSession):

    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        print('\nSelling Session starts...')
        name = self.ticketName()
        quantity = self.ticketQuantity()
        price = self.ticketPrice()
        date = self.ticketDate()


    # check if the ticketName valid
    def ticketName(self):
        count = 0
        while (count <= 60):
            name = input("Please enter the tickets' name you'd like to sell: ")
            if (not name == ""):
                # check if ticket name is alphanumeric and space only, check if space not the first or the last character.
                if all(x.isalnum() or x.isspace() for x in name):
                    # check if the name of the ticket is no longer than 60 characters
                    if (not name[0].isspace() and not name[-1].isspace()):
                        if (len(name) <= 60):
                            #print("valid")
                            return name
                            #break
                        else:
                            print("The ticket's name should less than 60 charaters")
                    else:
                        count += 1
                        print("Space not allow in first or last charater in ticket's name")
                else:
                    print("The name of the ticket has to be alphanumeric-only,")
                    count += 1
            else:
                count += 1

    def ticketQuantity(self):
        count = 0
        while (count <= 10):
            quantity = input("Please enter the quantity of the tickets you’d like to sell: ")
            if (not quantity == "" and quantity.isnumeric()):
                # The quantity of the tickets has to be more than 0, and less than or equal to 100
                if int(quantity) in range(1, 101):
                    #print("valid")
                    return quantity
                    #break
                else:
                    print("The quantity of the tickets has to be more than 0, and less than or equal to 100.")
                    count += 1
            else:
                print("Please enter the number")
                count += 1

    def ticketPrice(self):
        count = 0
        while (count <= 10):
            price = input("Price your ticket(s) to sell: ")
            if (not price == "" and price.isnumeric()):
                # Price has to be of range [10, 100]
                if int(price) in range(10, 101):
                    #print("valid")
                    return price
                    #break
                else:
                    print("Price has to be of range [10, 100]")
                    count += 1
            else:
                print("Please enter the number")
                count += 1

    def ticketDate(self):
        count = 0
        while (count <= 10):
            date = input("Date of Ticket YYYYMMDD (e.g. 20200202): ")
            if (not date == "" and date.isnumeric()):
                # Date must be given in the format YYYYMMDD (e.g. 20200901)
                if (len(date) == 8):
                    day = dt.datetime.strptime(date, '%Y%m%d').date()
                    # check if the valid date
                    if day > dt.datetime.today().date():
                        #print("valid " + date)
                        return date
                        #break
                    else:
                        print("Unavailable date")
                        count += 1
                else:
                    print("Date must be given in the format YYYYMMDD (e.g. 20200901)")
                    count += 1
            else:
                print("Date must be given in the format YYYYMMDD (e.g. 20200901)")
                count += 1

class BuySession(LoggedInSession):

    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        print('\nSelling Session start...')
        #self.ticketName()
        quantity, price = self.ticketName()
        balance = helpers.ResourcesHelper.getUserInfo()[self.username]['balence']
        quantity = self.ticketQuantity(quantity)
        newBalance = self.ticketPrice(price, quantity, balance)

    def findTicket(self,name):
        # if the valid ticket name, check if the name of ticket on selling
        for i in helpers.ResourcesHelper.getTicketInfo():
            # print(helpers.ResourcesHelper.getTicketInfo()[i]['name'])
            if helpers.ResourcesHelper.getTicketInfo()[i]['name'] == name:
                # check the available quantity of this ticket
                quantity = helpers.ResourcesHelper.getTicketInfo()[i]['number']
                price = helpers.ResourcesHelper.getTicketInfo()[i]['price']
                print("available ticket quantity for %s is " % name + str(quantity))
                return quantity, price,True

    # check if the ticketName valid
    def ticketName(self):
        count = 0
        #flag = False
        while (count <= 10):
            name = input("Please enter the tickets' name you'd like to buy.: ")
            if (not name == ""):
                # check if ticket name is alphanumeric and space only, check if space not the first or the last character.
                if all(x.isalnum() or x.isspace() for x in name):
                    # check if the name of the ticket is no longer than 60 characters
                    if (not name[0].isspace() and not name[-1].isspace()):
                        if (len(name) <= 60):
                            #print("valid input")
                            quantity, price, check = self.findTicket(name)
                            #print(check)
                            if check == True:
                                return quantity,price

                            count += 1
                            print("sorry, we do not have %s yet" % name)

                        else:
                            count += 1
                            print("The ticket's name should less than 60 charaters")
                    else:
                        count += 1
                        print("Space not allow in first or last charater in ticket's name")
                else:
                    print("The name of the ticket has to be alphanumeric-only")
                    count += 1
            else:
                count += 1

    def ticketQuantity(self, quantities):
        count = 0
        while (count <= 10):
            quantity = input("Please enter the quantity of the tickets you’d like to buy: ")
            if (not quantity == "" and quantity.isnumeric()):
                # The quantity of the tickets has to be more than 0, and less than or equal to the available quantity
                if int(quantity) in range(1, quantities+1):
                    #print("valid")
                    return quantity
                    #break
                else:
                    print("The quantity of the tickets has to be more than 0, and less than or equal to 100.")
                    count += 1
            else:
                print("Please enter the number")
                count += 1

    # The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)
    def ticketPrice(self, price, quantities, balance):
        ticket_price = 1.05 * ((1.35 * float(price)) * float(quantities))
        balance_now = float(balance) - ticket_price
        if balance_now >= 0:
            #print("valid")
            print("Total price: ", ticket_price)
            return balance_now
        else:
            print("Balance not enough, still need: $", str(balance_now))

