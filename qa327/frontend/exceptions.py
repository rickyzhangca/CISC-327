'''
This is the exceptions module:
'''


'''
Exception of when user do not have the access to certain pages.
'''
class CannotAccessPageException(Exception):
    pass


'''
Exception of when the user input format is wrong.
'''
class WrongFormatException(Exception):
    pass