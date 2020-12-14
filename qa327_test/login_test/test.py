import tempfile
from importlib import reload
import os
import io
import sys

path = os.path.dirname(os.path.abspath(__file__))

sys.path.append('qa327/frontend')
import app

################################################################
# if want to force printing to console:
# pritn(something)
# assert false
################################################################

def test_r3_1_1(capsys): # Check if the login command is invalid when user has logged in
    helper(capsys=capsys, test_id='r3_1_1')

def test_r3_2_1(capsys): # Check if the user can login when no user has logged in
    helper(capsys=capsys, test_id='r3_2_1')

def test_r3_3_1(capsys): # Check if the session ask for the user's email to login
    helper(capsys=capsys, test_id='r3_3_1')

def test_r3_3_2(capsys): # Check if the session ask for the user's password after email has been provided
    helper(capsys=capsys, test_id='r3_3_2')

def test_r3_4_1(capsys): # Check if a valid email can be accepted in the login session
    helper(capsys=capsys, test_id='r3_4_1')

def test_r3_4_2(capsys): # Check if a valid password can be accepted in the login session
    helper(capsys=capsys, test_id='r3_4_2')

def test_r3_4_3(capsys): # Check if a invalid email can be rejected
    helper(capsys=capsys, test_id='r3_4_3')

def test_r3_4_4(capsys): # Check if a invalid password can be rejected
    helper(capsys=capsys, test_id='r3_4_4')

def test_r3_5_1(capsys): # Check if the error message can be returned and end the session if there is formatting error in email or password
    helper(capsys=capsys, test_id='r3_5_1')

def test_r3_6_1(capsys): # Check if the massage 'Account logged in.' shows up snf returns to the landing screen, if the login info are correct
    helper(capsys=capsys, test_id='r3_6_1')

def test_r3_6_2(capsys): # Otherwise, show message 'Login failed.', end login session/process, and print the landing screen according to R1, if the password does not match the email
    helper(capsys=capsys, test_id='r3_6_2')

def helper(
        capsys,
        test_id):
    """ a helper function that test requirements for the example app

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """

    # cleanup package
    reload(app)

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
        'app.py', 'Kingston',
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

    # compare transactions:
    with open(transaction_summary_file, 'r') as of:
        content = of.read()
        with open(os.path.join(case_folder, 'transaction_summary_file.csv'), 'r') as exp_file_of:
            expected_content = exp_file_of.read()
            assert content == expected_content

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
