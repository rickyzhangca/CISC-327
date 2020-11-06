from loggedInSession import LoggedInSession

class UpdateSession(LoggedInSession):

    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        print('\nUpdateSession...')
