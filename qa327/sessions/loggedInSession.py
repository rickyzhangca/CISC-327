from session import Session
from landing import LandingSession

class LoggedInSession(Session):

    def __init__(self, username):
        super().__init__(username)   
        if not username:
            print('Invaild command, user must be logged in first')
            raise Exception('User Not Logged In')
    
    def routing(self):
        return LandingSession(self.username)
        
    def getBalence(self):
        pass

    def getMenu(self):
        return 'buy, sell, update, and logout'