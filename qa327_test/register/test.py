import tempfile
from importlib import reload
import os
import io
import sys
import pytest

path = os.path.dirname(os.path.abspath(__file__))

sys.path.append('qa327/frontend')
import app

################################################################
# if want to force printing to console:
# print(something)
# assert false
################################################################

'''
subfolders = [ f.name for f in os.scandir('qa327_test/register') if f.is_dir() ].remove('__pycache__')
print(subfolders)
@pytest.mark.parametrize('id',subfolders)
def test_me(capsys, id):
    helper(
        capsys=capsys,
        test_id=id
    )
'''

def test_r2_1(capsys): # Check if the register command is invalid when the user has logged in	
    helper(capsys=capsys, test_id='r2_1')

def test_r2_2(capsys): # Check if the program starts a registration session following register command, given there is not a user logged in	
    helper(capsys=capsys, test_id='r2_2')

def test_r2_3_1(capsys): # Check if the poragm will ask for email first	
    helper(capsys=capsys, test_id='r2_3_1')

def test_r2_3_2(capsys): # Check if the poragm will ask for email, followed by username in a registration session	
    helper(capsys=capsys, test_id='r2_3_2')

def test_r2_3_3(capsys): # Check if the poragm will ask for email, username, followed by password in a registration session	
    helper(capsys=capsys, test_id='r2_3_3')

def test_r2_3_4(capsys): # Check if the poragm will ask for password confirmation in the end of a registration session
    helper(capsys=capsys, test_id='r2_3_4')

def test_r2_4_1(capsys): # Check if the program displays error when email is empty and ask the user to enter it in order to proceed
    helper(capsys=capsys, test_id='r2_4_1')

def test_r2_4_2(capsys): # Check if the program displays error when password is empty and ask the user to enter it in order to proceed
    helper(capsys=capsys, test_id='r2_4_2')

def test_r2_5_1(capsys): # Check if the program proceeds when email address user entered meets RFC 5322 standard
    helper(capsys=capsys, test_id='r2_5_1')

def test_r2_5_2(capsys): # Check if the program proceeds when email address user entered meets RFC 5322 standard
    helper(capsys=capsys, test_id='r2_5_2')
    
def test_r2_5_3(capsys): # Check if the program proceeds when email address user entered meets RFC 5322 standard
    helper(capsys=capsys, test_id='r2_5_3')

def test_r2_5_4(capsys): # Check if the program displays error when the email address user entered does not meet RFC 5322 standard
    helper(capsys=capsys, test_id='r2_5_4')

def test_r2_5_5(capsys): # Check if the program displays error when the email address user entered does not meet RFC 5322 standard
    helper(capsys=capsys, test_id='r2_5_5')

def test_r2_5_6(capsys): # Check if the program displays error when the email address user entered does not meet RFC 5322 standard
    helper(capsys=capsys, test_id='r2_5_6')

def test_r2_5_7(capsys): # Check if the program displays error when the email address user entered does not meet RFC 5322 standard
    helper(capsys=capsys, test_id='r2_5_7')

def test_r2_5_8(capsys): # Check if the program displays error when the email address user entered does not meet RFC 5322 standard
    helper(capsys=capsys, test_id='r2_5_8')

def test_r2_5_9(capsys): # Check if the program displays error when the email address user entered does not meet RFC 5322 standard
    helper(capsys=capsys, test_id='r2_5_9')

def test_r2_6_1(capsys): # Check if the program proceeds when password user entered meets the requirements
    helper(capsys=capsys, test_id='r2_6_1')

def test_r2_6_2(capsys): # Check if the program displays error when the password user entered does not meet the requirements
    helper(capsys=capsys, test_id='r2_6_2')

def test_r2_6_3(capsys): # Check if the program displays error when the password user entered does not meet the requirements
    helper(capsys=capsys, test_id='r2_6_3')

def test_r2_6_4(capsys): # Check if the program displays error when the password user entered does not meet the requirements
    helper(capsys=capsys, test_id='r2_6_4')

def test_r2_7_1(capsys): # Check if the program proceeds when the user confirmed the password by entering the same characters again
    helper(capsys=capsys, test_id='r2_7_1')

def test_r2_7_2(capsys): # Check if the program displays error when the user entered different characters
    helper(capsys=capsys, test_id='r2_7_2')

def test_r2_7_3(capsys): # Check if the program displays error when the user entered different characters
    helper(capsys=capsys, test_id='r2_7_3')

def test_r2_8_1(capsys): # Check if the program proceeds when username user entered meets the requirements
    helper(capsys=capsys, test_id='r2_8_1')
    
def test_r2_8_2(capsys): # Check if the program proceeds when username user entered meets the requirements
    helper(capsys=capsys, test_id='r2_8_2')
    
def test_r2_8_3(capsys): # Check if the program displays error when username user entered has symbol
    helper(capsys=capsys, test_id='r2_8_3')
    
def test_r2_8_4(capsys): # Check if the program displays error when username user entered is empty
    helper(capsys=capsys, test_id='r2_8_4')
    
def test_r2_8_5(capsys): # Check if the program displays error when username user entered has a space at the beginning
    helper(capsys=capsys, test_id='r2_8_5')
    
def test_r2_8_6(capsys): # Check if the program displays error when username user entered has a space at the tail
    helper(capsys=capsys, test_id='r2_8_6')
    
def test_r2_9_1(capsys): # Check if the program proceeds when username user entered meets the requirements
    helper(capsys=capsys, test_id='r2_9_1')
    
def test_r2_9_2(capsys): # Check if the program displays error when username user entered is less than 2 characters long
    helper(capsys=capsys, test_id='r2_9_2')
    
def test_r2_9_3(capsys): # Check if the program displays error when username user entered is longer than 20 characters long
    helper(capsys=capsys, test_id='r2_9_3')
    
def test_r2_10_1(capsys): # Check if the program proceeds when email user has not been used before
    helper(capsys=capsys, test_id='r2_10_1')
    
def test_r2_10_2(capsys): # Check if the program displays error when email user has been used before
    helper(capsys=capsys, test_id='r2_10_2')
    
def test_r2_11_1(capsys): # Check if the formatting error is displayed when user entered an email in incorrect format
    helper(capsys=capsys, test_id='r2_11_1')
    
def test_r2_11_2(capsys): # Check if the formatting error is displayed when user entered a username in incorrect format
    helper(capsys=capsys, test_id='r2_11_2')
    
def test_r2_11_3(capsys): # Check if the formatting error is displayed when user entered a password in incorrect format
    helper(capsys=capsys, test_id='r2_11_3')
    
def test_r2_12(capsys): # Check if the program proceeds after the user entered valid email, username, and passwords
    helper(capsys=capsys, test_id='r2_12')

def test_r2_13(capsys): # Check if the program gives the user a starting balance
    helper(capsys=capsys, test_id='r2_13')

def test_r2_14(capsys): # Check if the program starts a landing session after an account is registered
    helper(capsys=capsys, test_id='r2_14')

def helper(capsys, test_id):
    """ a helper function that test requirements for the example app

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """

    # cleanup package
    reload(app)
    if os.path.exists("Kingston_transactions.csv"): 
        os.remove("Kingston_transactions.csv")

    # locate test case folder:
    case_folder = os.path.join(path, test_id)

    # read terminal input: 
    with open(
        os.path.join(
            case_folder, 'terminal_input.txt')) as rf:
        terminal_input = rf.read().splitlines()

    # read expected tail portion of the terminal output:
    with open(
        os.path.join(
            case_folder, 'terminal_output_tail.txt')) as rf:
        terminal_output_tail = rf.read().splitlines()

    # create a temporary file in the system to store output transactions
    temp_fd, temp_file = tempfile.mkstemp()
    transaction_summary_file = temp_file

    # prepare program parameters
    sys.argv = [
        'app.py', 'kingston',
        os.path.join(case_folder, 'valid_account_list_file.csv'),
        os.path.join(case_folder, 'valid_ticket_list_file.csv'),]

    # set terminal input
    sys.stdin = io.StringIO(
        '\n'.join(terminal_input))

    # run the program
    app.main()

    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()

    # compare terminal outputs at the end.`
    for i in range(1, len(terminal_output_tail)+1):
        index = i * -1
        assert terminal_output_tail[index] == out_lines[index]

    '''
    # compare transactions:
    with open('Kingston_transactions.csv', 'r') as of:
        content = of.read()
        with open(os.path.join(case_folder, 'transaction_summary_file.csv'), 'r') as exp_file_of:
            expected_content = exp_file_of.read()
            assert content == expected_content
    '''

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
    if os.path.exists("Kingston_transactions.csv"): 
        os.remove("Kingston_transactions.csv")
