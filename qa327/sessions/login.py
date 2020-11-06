from unloggedInSession import UnloggedInSession
from landing import LandingSession

from _helper import getUserInfo

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
        user_info = getUserInfo()
        for i in user_info:
            if user_info[i]['email'] == email and user_info[i]['password'] == password:
                print('Account logged in.')
                self.username = i
                return
        print('Email or password incorrect.')