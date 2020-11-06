import helpers
import exceptions

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
        print('\nRegister Session...')
    
    def authorize(self, username, password):
        self.username = username


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
        print('\nUpdateSession...')


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