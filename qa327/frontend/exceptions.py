'''
This is the exceptions module:
'''


'''
Exception of when user do not have the access to certain pages.
'''
class CannotAccessPageException(Exception):
    pass

'''
Exception of the first password and the second password does not match during registration.
'''
class PasswordsNotMatchingException(Exception):
    pass

'''
Exception of when the user input format is wrong.
'''
class WrongFormatException(Exception):
    def __init__(self, message=''):
        super().__init__('{}, format is incorrect.'.format(message))

'''
Exception of when the ticket name is wrong.
'''
class WrongTicketNameException(Exception):
    pass

'''
Exception of when the ticket quantity is wrong.
'''
class WrongTicketQuantityException(Exception):
    pass

'''
Exception of when the ticket quantity is wrong.
'''
class WrongTicketPriceException(Exception):
    pass

'''
Exception of when the email already exists in user data (already registered).
'''
class EmailAlreadyExistsException(Exception):
    pass