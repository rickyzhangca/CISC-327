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
    pass

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

'''
Exception of when the date is impossible.
'''
class WrongDateException(Exception):
    pass