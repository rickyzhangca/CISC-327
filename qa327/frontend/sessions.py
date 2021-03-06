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
    # If logged in, show the menu item buy, sell, update, and logout. Also, print out the user's balance.
    # raise exceptions if user have not logged in.
    def __init__(self, username):
        super().__init__(username)   
        if not username:
            print('\nInvaild command, user must be logged in first')
            raise exceptions.CannotAccessPageException()
    
    def routing(self):
        return LandingSession(self.username)

    def getMenu(self):
        return 'buy, sell, update, and logout'


'''
Base class for sessions that does not required login.
'''
class UnloggedInSession(Session):
    # if not logged in, show the menu item login, register, and exits.
    # raise exceptions if user have logged in.
    def __init__(self, username): 
        super().__init__() 
        if username:
            print('\nInvaild command, user must be logged out first')
            raise exceptions.CannotAccessPageException()

    def routing(self):
        return LandingSession()

    def getMenu(self):
        return 'login, register, and exits'


'''
Landing page that displays usermenu and balance.
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
                print('\nCommand undefind.')
                new_session = self
        except exceptions.CannotAccessPageException:
            new_session = self
        return new_session
    
    def operate(self):
        print('\nLanding Screen...')        
        self.showbalance()
        self.displayMenu()
        self.getUserCommand()
    
    # display user menu depend on whether the user logged in.
    def displayMenu(self):
        print('Menu options - ', end = '')
        if self.username:
            print(LoggedInSession.getMenu(self))
        else:
            print(UnloggedInSession.getMenu(self))

    def showbalance(self):
        if self.username:
            print('Hi', self.username + '!')
            print('Your balance is: $' + str(helpers.ResourcesHelper.getUserInfo()[self.username]['balance']) + '.\n')

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
        #check email
        try:
            email = helpers.UserIOHelper.acceptEmail()
            password = helpers.UserIOHelper.acceptPassword()            
            self.authorize(email, password)
        except exceptions.WrongFormatException as e:
            print(str(e))
            print('\nLogin failed, ending session...')
    
    # authorize email and password the user inputed. Setup username. 
    def authorize(self, email, password):
        for i in helpers.ResourcesHelper.getUserInfo():
            if helpers.ResourcesHelper.getUserInfo()[i]['email'] == email and helpers.ResourcesHelper.getUserInfo()[i]['password'] == password:
                print('\nAccount logged in!')
                self.username = i
                return
        print('\nEmail or password incorrect.')


'''
user register
'''
class RegisterSession(UnloggedInSession):

    def __init__(self, username):
        super().__init__(username)
        self.username = None
    
    def operate(self):
        try:
            user_email = helpers.UserIOHelper.acceptEmail()

            if self.checkExistence(user_email):
                raise exceptions.EmailAlreadyExistsException()

            user_name = helpers.UserIOHelper.acceptUserName()
            user_password = helpers.UserIOHelper.acceptPassword()
            user_password2 = helpers.UserIOHelper.acceptPassword2()
            if user_password != user_password2:
                raise exceptions.PasswordsNotMatchingException()
            self.addNewUser(user_name, user_email, user_password)

        except exceptions.EmailAlreadyExistsException: 
            print('\nThis email already exists in the system')
            print('\nRegistration failed, ending session...')
        except exceptions.PasswordsNotMatchingException: 
            print('\nThe password entered first time does not match the one enter the second time.')
            print('\nRegistration failed, ending session...')
        except exceptions.WrongFormatException as e:
            print(str(e))
            print('\nRegistration failed, ending session...')
    
    def checkExistence(self, user_email):
        for i in helpers.ResourcesHelper.getUserInfo():
            if user_email == helpers.ResourcesHelper.getUserInfo()[i]['email']:
                return True
        return False

    def addNewUser(self, user_name, user_email, user_password):
        helpers.TransactionsHelper.newUserTransaction("register", user_name, user_email, user_password, 3000)
        print('\nRegistered successfully.')

'''
update ticket
'''
class UpdateSession(LoggedInSession):
    # only appear after user logged in
    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        try:
            ticket_name = helpers.UserIOHelper.acceptTicketName()
            ticket_quantity = helpers.UserIOHelper.acceptTicketQuantity()
            ticket_price = helpers.UserIOHelper.acceptTicketPrice()
            ticket_date = helpers.UserIOHelper.acceptDate()
            if ticket_name not in helpers.ResourcesHelper.getTicketInfo():
                raise exceptions.WrongTicketNameException
            self.updateTicket(ticket_name, ticket_price, ticket_quantity, ticket_date)        
        except exceptions.WrongFormatException as e:     
            print(str(e))
            print('\nUpdate failed, ending session...')
        except exceptions.WrongTicketNameException:
            print('\nThe ticket name you entered cannot be found, ending session...')

    def updateTicket(self, ticket_name, ticket_price, ticket_quantity, ticket_date):
        helpers.TransactionsHelper.newTicketTransaction("update", self.username, ticket_name, ticket_price, ticket_quantity, ticket_date)
        helpers.ResourcesHelper.getTicketInfo()[ticket_name]['price'] = ticket_price
        helpers.ResourcesHelper.getTicketInfo()[ticket_name]['number'] = ticket_quantity
        helpers.ResourcesHelper.getTicketInfo()[ticket_name]['date'] = ticket_date

'''
User logout.
'''
class LogoutSession(LoggedInSession):
    # only appear after user logged in
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
    # only appear after user not logged in
    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        print('\nSaving transactions & exit...')

    def routing(self):
        return None


'''
Selling session.
'''
class SellSession(LoggedInSession):
    # only appear after user logged in
    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        print('\nSelling Session starts...')
        try:
            ticket_name = helpers.UserIOHelper.acceptTicketName()
            if ticket_name in helpers.ResourcesHelper.getTicketInfo():
                raise exceptions.WrongTicketNameException
            ticket_quantity = helpers.UserIOHelper.acceptTicketQuantity()
            ticket_price = helpers.UserIOHelper.acceptTicketPrice()
            ticket_date = helpers.UserIOHelper.acceptDate()
            self.addNewTicket(ticket_name, ticket_price, ticket_quantity, ticket_date)
        except exceptions.WrongFormatException as e:
            print(str(e))
            print('\nAdd new ticket failed, ending session...')
        except exceptions.WrongTicketNameException:
            print('\nTicket with this name already exist, ending session...')        
        except exceptions.WrongTicketQuantityException:
            print('\nThe ticket quantity you entered is not available, ending session...')
        except exceptions.WrongTicketPriceException as e:
            print(str(e))
            print('\nThe ticket price you entered is not available, ending session...')        
    
    def addNewTicket(self, ticket_name, ticket_price, ticket_quantity, ticket_date):
        helpers.TransactionsHelper.newTicketTransaction("sell", self.username, ticket_name, ticket_price, ticket_quantity, ticket_date)
        helpers.ResourcesHelper.getTicketInfo()[ticket_name] = {
            'price': ticket_price,
            'number': ticket_quantity,
            'email': helpers.ResourcesHelper.getUserInfo()[self.username]['email'],
            'date': ticket_date
        }
        print('\nTicket info added successfully.')


'''
Buying session.
'''
class BuySession(LoggedInSession):

    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        print('\nBuying Session starts...')
        self.printTicketList()
        try:
            ticket_name = helpers.UserIOHelper.acceptTicketName()            
            if ticket_name not in helpers.ResourcesHelper.getTicketInfo():
                raise exceptions.WrongTicketNameException
            ticket_quantity = helpers.UserIOHelper.acceptTicketQuantity()
            if ticket_quantity > helpers.ResourcesHelper.getTicketInfo()[ticket_name]['number']:
                raise exceptions.WrongTicketQuantityException
            ticket_price = helpers.ResourcesHelper.getTicketInfo()[ticket_name]['price']
            if self.checkBalance(ticket_price, ticket_quantity):
                self.processOrder(ticket_name, ticket_price, ticket_quantity)
            else:
                print('\nInsufficient funds, ending session...')
        except exceptions.WrongFormatException as e:
            print(str(e))
            print('\nBuy ticket failed, ending session...')
        except exceptions.WrongTicketNameException:
            print('\nThe ticket name you entered cannot be found, ending session...')
        except exceptions.WrongTicketQuantityException:
            print('\nThe ticket quantity you entered is not available, ending session...')           
    
    def printTicketList(self):
        print('\nTicket avilable:\nTicket Name\tPrice\tNumber\tDate')
        for i in helpers.ResourcesHelper.getTicketInfo():
            print(i + '\t' + str(helpers.ResourcesHelper.getTicketInfo()[i]['price']) + '\t' + str(helpers.ResourcesHelper.getTicketInfo()[i]['number']) + '\t' + str(helpers.ResourcesHelper.getTicketInfo()[i]['date']))
    
    def checkBalance(self, ticket_price, ticket_quantity):
        return helpers.ResourcesHelper.getUserInfo()[self.username]['balance'] >= ticket_price * ticket_quantity

    def processOrder(self, ticket_name, ticket_price, ticket_quantity):
        helpers.ResourcesHelper.getUserInfo()[self.username]['balance'] -= ticket_price * ticket_quantity
        helpers.ResourcesHelper.getTicketInfo()[ticket_name]['number'] -= ticket_quantity
        helpers.TransactionsHelper.newTicketTransaction("buy", self.username, ticket_name, ticket_price, ticket_quantity, helpers.ResourcesHelper.getTicketInfo()[ticket_name]['date'])        
        print('\nTicket "' + ticket_name + '" sold successfully.')