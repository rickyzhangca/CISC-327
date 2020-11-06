from loggedInSession import LoggedInSession

class SellSession(LoggedInSession):

    def __init__(self, username):
        super().__init__(username)

    def operate(self):
        print('\nSellSession...')