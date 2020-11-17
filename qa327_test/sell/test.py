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

# Check if the selling command invalid when user has not logged in
def test_sell01(capsys): # example case
    helper(
        capsys=capsys,
        test_id='r4_0_1'
    )
# Check if the selling session start when user has logged in
def test_sell02(capsys): # example case
    helper(
        capsys=capsys,
        test_id='r4_0_2'
    )
# Check if a valid ticket name can be accepted in the selling session
def test_sell11(capsys): # example case
    helper(
        capsys=capsys,
        test_id='r4_1_1'
    )
# Check if a not alphanumeric-only ticket name not be accepted in the selling session
def test_sell12(capsys): # example case
    helper(
        capsys=capsys,
        test_id='r4_1_2'
    )
# Check if the first character of name is space not be accepted in the selling session
def test_sell13(capsys): # example case
    helper(
        capsys=capsys,
        test_id='r4_1_3'
    )
# Check if the last character of name is space not be accepted in the selling session
def test_sell131(capsys): # example case
    helper(
        capsys=capsys,
        test_id='r4_1_3_1'
    )
# Check if the name of the ticket is longer than 60 characters not be accepted in the selling session
def test_sell14(capsys): # example case
    helper(
        capsys=capsys,
        test_id='r4_1_4'
    )
# Check if the valid quantity can be accepted in the selling session
def test_sell21(capsys): # example case
    helper(
        capsys=capsys,
        test_id='r4_2_1'
    )
# Check if the quantity of the tickets is more than 100 not be accepted in the selling session
def test_sell22(capsys): # example case
    helper(
        capsys=capsys,
        test_id='r4_2_2'
    )
# Check if the quantity of the tickets is less than 0 not be accepted in the selling session
def test_sell23(capsys): # example case
    helper(
        capsys=capsys,
        test_id='r4_2_3'
    )
# Check if the quantity of the tickets is equal to 0 not be accepted in the selling session
def test_sell231(capsys): # example case
    helper(
        capsys=capsys,
        test_id='r4_2_3_1'
    )
# Check if the valid price can be accepted in the selling session
def test_sell31(capsys): # example case
    helper(
        capsys=capsys,
        test_id='r4_3_1'
    )
# Check if the valid date can be accepted in the selling session
def test_sell41(capsys): # example case
    helper(
        capsys=capsys,
        test_id='r4_4_1'
    )
# Check if the incorrect format date not be accepted in the selling session
def test_sell42(capsys): # example case
    helper(
        capsys=capsys,
        test_id='r4_4_2'
    )
# Check if the selling session work when every input valid
def test_sell(capsys): # example case
    helper(
        capsys=capsys,
        test_id='sell_example'
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
