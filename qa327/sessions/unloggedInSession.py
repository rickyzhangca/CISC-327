from session import Session
from landing import LandingSession

class UnloggedInSession(Session):

    def __init__(self, username = None): 
        super().__init__() 
        if username:
            print('Invaild command, user must be logged out first')
            raise Exception('User Logged In')

    def routing(self):
        return LandingSession()

    def getMenu(self):
        return 'login, register, and exits'