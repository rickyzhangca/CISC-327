import helpers

'''
This is the sessions module
'''

class Session:

    def __init__(self, username = None):
        self.username = username

    def routing(self):
        return self

    def operate(self):
        pass


class LandingSession(Session):

    def __init__(self, username = None):
        super().__init__(username)
    
    def routing(self):
        #different routing for each case
        if self.username:
            # if loogged in
            LoggedInSession.routing(self)
        else:
            # if not logged in yet
            UnloggedInSession.routing(self)
    
    def operate(self):
        print('\nLanding...')
        self.displayMenu()
        self.showBalence()
        self.getUserCommand()
    
    def displayMenu(self):
        # for different log in status， the input requirement is also different。
        if self.username:
            print(LoggedInSession.getMenu(self))
        else:
            print(UnloggedInSession.getMenu(self))

    def showBalence(self):
        if self.username:
            print('Your balance is:', helpers.ResourcesHelper.getUserInfo()[self.username]['balence'])

    def getUserCommand(self):
        self.command = input('Your command: ')


class LoggedInSession(Session):

    def __init__(self, username):
        super().__init__(username)   
        if not username: # check log in status
            print('Invaild command, user must be logged in first')
            raise Exception('User Not Logged In')
    
    def routing(self):
        # if user logged in, no commads other than "buy" "sell""log out" are accepted
        UpdateSession(self.username) #print out update status (update is not a command)
        if self.command == 'buy':
            new_session = BuySession(self.username)
        elif self.command == 'sell':
            new_session = SellSession(self.username)
        elif self.command == 'logout':
            new_session = LogoutSession(self.username)
        elif self.command == 'exits':
            new_session = ExitSession(self.username)
        else:
            print('Command undefind.')
            new_session = self
        return LandingSession(self.username)
        
    def getBalence(self):
        pass

    def getMenu(self):
        return 'buy, sell, update, and logout'


class UnloggedInSession(Session):

    def __init__(self, username = None): 
        super().__init__() 
        if username: #check log in status
            print('Invaild command, user must be logged out first')
            raise Exception('User Logged In')

    def routing(self): #get the not-loggedin routing
        # if user not loggedin, no command other thaan login register is accepted
        if self.command == 'login':
            new_session = LoginSession()
        elif self.command == 'register':
            new_session = RegisterSession()
        elif self.command == 'exits':
            new_session = ExitSession(self.username)
        else:
            print('Command undefind.')
            new_session = self
        return LandingSession()

    def getMenu(self):
        return 'login, register, and exits'


class LoginSession(UnloggedInSession):

    def __init__(self):
        super().__init__()
        self.username = None
    
    def routing(self):
        return LandingSession(self.username)
    
    def operate(self):
        print('\nLog in session starts...')
        email = input('Email: ')
        password = input('Password: ')
        self.authorize(email, password)
    
    def authorize(self, email, password):
        for i in helpers.ResourcesHelper.getUserInfo():
            if helpers.ResourcesHelper.getUserInfo()[i]['email'] == email and helpers.ResourcesHelper.getUserInfo()[i]['password'] == password:
                print('Account logged in.')
                self.username = i
                return
        print('Email or password incorrect.')

class RegisterSession(UnloggedInSession):

    def __init__(self):
        super().__init__()
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


class LogoutSession(LoggedInSession):

    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        print('\nLogoutSession...')

    def routing(self):
        return LandingSession(None)

class ExitSession(UnloggedInSession):

    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        print('\nExitSession...')

    def routing(self):
        return None
