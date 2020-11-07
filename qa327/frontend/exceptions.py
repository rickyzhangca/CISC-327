'''
This is the exceptions module:
'''


'''
Exception of when user do not have the access to certain pages.
'''
class CannotAccessPageException(Exception):
    pass

'''
Exception of unknown error.
'''
class UnknownException(Exception):
    pass

'''
Exception of when the user input format is wrong.
'''
class WrongFormatException(Exception):
    def __init__(self, message=''):
        super().__init__('{} format is incorrect.'.format(message))

'''
Exception of when the ticket quantity is wrong.
'''
class WrongTicektQuantityException(Exception):
    pass

'''
Exception of when the ticket quantity is wrong.
'''
class WrongTicektPriceException(Exception):
    pass