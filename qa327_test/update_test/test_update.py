import tempfile
from importlib import reload
import os
import io
import sys
import unittest

path = os.path.dirname(os.path.abspath(__file__))

sys.path.append('qa327/frontend')
import app

################################################################
# if want to force printing to console:
# pritn(something)
# assert false
################################################################

def test_r6_1(capsys): # valid test for update
    helper(
        capsys=capsys,
        test_id='r6_1'
    )

def test_r6_2(capsys): # invalid test for update when have invalid name input
    helper(
        capsys=capsys,
        test_id='r6_2'
    )

def test_r6_3(capsys): # invalid test for update when have invalid quantity input
    helper(
        capsys=capsys,
        test_id='r6_3'
    )

def test_r6_4(capsys): # invalid test for update when have invalid price input(negative number)
    helper(
        capsys=capsys,
        test_id='r6_4'
    )

def test_r6_5(capsys): # invalid test for update when have invalid price input(too large number)
    helper(
        capsys=capsys,
        test_id='r6_5'
    )

def test_r6_6(capsys): # invalid test for update when have invalid price input(too large number)
    helper(
        capsys=capsys,
        test_id='r6_6'
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

