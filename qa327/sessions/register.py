from unloggedInSession import UnloggedInSession

class RegisterSession(UnloggedInSession):

    def __init__(self):
        super().__init__()
        self.username = None
    
    def operate(self):
        print('\nRegister Session...')
    
    def authorize(self, username, password):
        self.username = username