from session import Session

from loggedInSession import LoggedInSession
from unloggedInSession import UnloggedInSession

from login import LoginSession
from register import RegisterSession
from buy import BuySession
from sell import SellSession
from update import UpdateSession
from logout import LogoutSession
from exits import ExitSession

from _helper import getUserInfo

class LandingSession(Session):

    def __init__(self, username = None):
        super().__init__(username)
    
    def routing(self):
        if self.command == 'login':
            new_session = LoginSession()
        elif self.command == 'register':
            new_session = RegisterSession()
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
        return new_session
    
    def operate(self):
        print('\nLanding...')
        self.displayMenu()
        self.showBalence()
        self.getUserCommand()
    
    def displayMenu(self):
        if self.username:
            print(LoggedInSession.getMenu(self))
        else:
            print(UnloggedInSession.getMenu(self))

    def showBalence(self):
        if self.username:
            print('Your balance is:', getUserInfo()[self.username]['balence'])

    def getUserCommand(self):
        self.command = input('Your command: ')