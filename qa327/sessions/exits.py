from unloggedInSession import UnloggedInSession

class ExitSession(UnloggedInSession):

    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        print('\nExitSession...')

    def routing(self):
        return None