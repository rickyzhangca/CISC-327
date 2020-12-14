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
# Check if the buying action succeed if user input is valid
def test_buy_example(capsys): 
    helper(
        capsys=capsys,
        test_id='buy_example'
    )
# Check if the selling command invalid when user has not logged in
def test_buy01(capsys):
    helper(
        capsys=capsys,
        test_id='r5_0_1'
    )
# Check if the selling command valid when user has logged in
def test_buy02(capsys):
    helper(
        capsys=capsys,
        test_id='r5_0_2'
    )
# Check if a valid ticket name can be accepted in the selling session
def test_buy11(capsys):
    helper(
        capsys=capsys,
        test_id='r5_1_1'
    )
#Check if a not alphanumeric-only ticket name not be accepted in the selling session
def test_buy12(capsys):
    helper(
        capsys=capsys,
        test_id='r5_1_2'
    )
#Check if the first character of name is space not be accepted in the selling session
def test_buy13(capsys):
    helper(
        capsys=capsys,
        test_id='r5_1_3'
    )
#Check if the last character of name is space not be accepted in the selling session
def test_buy131(capsys):
    helper(
        capsys=capsys,
        test_id='r5_1_3_1'
    )
# Check if the name of the ticket is longer than 60 characters not be accepted in the selling session
def test_buy14(capsys):
    helper(
        capsys=capsys,
        test_id='r5_1_4'
    )
# Check if the name of the ticket is not exists in the database not accepted in the selling section
def test_buy15(capsys):
    helper(
        capsys=capsys,
        test_id='r5_1_5'
    )
# Check if the quantity of the tickets is less than 0 not be accepted in the selling session
def test_buy21(capsys):
    helper(
        capsys=capsys,
        test_id='r5_2_1'
    )
# Check if the quantity of the tickets is equal to 0 not be accepted in the selling session
def test_buy211(capsys):
    helper(
        capsys=capsys,
        test_id='r5_2_1_1'
    )
# Check if the quantity of the tickets is more than available quantity not be accepted in the selling session
def test_buy22(capsys):
    helper(
        capsys=capsys,
        test_id='r5_2_2'
    )

# Check if the buying action failed if user has not enough balance.
def test_buy31(capsys):
    helper(
        capsys=capsys,
        test_id='r5_3_1'
    )
# Check if the buying action succeed if user has enough balance.
def test_buy32(capsys):
    helper(
        capsys=capsys,
        test_id='r5_3_2'
    )

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

    # compare transactions:
    with open(transaction_summary_file, 'r') as of:
        content = of.read()
        with open(os.path.join(case_folder, 'transaction_summary_file.csv'), 'r') as exp_file_of:
            expected_content = exp_file_of.read()
            assert content == expected_content

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
