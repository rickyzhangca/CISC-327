from loggedInSession import LoggedInSession
from landing import LandingSession

class LogoutSession(LoggedInSession):

    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        print('\nLogoutSession...')

    def routing(self):
        return LandingSession(None)