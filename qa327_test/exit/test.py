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

def test_r7_1(capsy): #example of valid buy session
    helper(
        capsys=capsys,
        test_id='r1_1'
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

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
