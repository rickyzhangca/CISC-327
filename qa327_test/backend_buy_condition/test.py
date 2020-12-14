import tempfile
from importlib import reload
import os
import io
import sys

path = os.path.dirname(os.path.abspath(__file__))

sys.path.append('qa327')
import app

################################################################
# if want to force printing to console:
# pritn(something)
# assert false
################################################################
# Check if the buying action succeed if user input is valid
def conditionFalse(capsys): 
    helper(
        capsys=capsys,
        test_id='condition=false'
    )

def conditionTrue(capsys): 
    helper(
        capsys=capsys,
        test_id='condition=true'
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

    # read transacrion file and rewrite later:
    with open(
        os.path.join(
            case_folder, 'kingston_transactions.csv')) as rf:
        kst = rf.read().splitlines()

    # read transacrion file and rewrite later:
    with open(
        os.path.join(
            case_folder, 'montreal_transactions.csv')) as rf:
        mtl = rf.read().splitlines()

    # read transacrion file and rewrite later:
    with open(
        os.path.join(
            case_folder, 'toronto_transactions.csv')) as rf:
        trt = rf.read().splitlines()

    # prepare program parameters
    sys.argv = ['backend2/bakend.py']

    # run the program
    app.main()

    # read expected files:
    with open(
        os.path.join(
            case_folder, 'expected_accounts.csv')) as rf:
        expected_account = rf.read().splitlines()

    with open(
        os.path.join(
            case_folder, 'expected_ticket.csv')) as rf:
        expected_ticket = rf.read().splitlines()

    # read actual updated file:
    with open(
        os.path.join(
            case_folder, 'updated_accounts.csv')) as rf:
        actual_updated_accounts = rf.read().splitlines()

    with open(
        os.path.join(
            case_folder, 'updated_tickets.csv')) as rf:
        actual_updated_tickets = rf.read().splitlines()

    # compare updated acconut at the end.`
    for i in range(1, len(expected_account)+1):
        index = i * -1
        assert expected_account[index] == actual_updated_accounts[index]

    # compare updated ticket at the end.`
    for i in range(1, len(expected_ticket)+1):
        index = i * -1
        assert expected_ticket[index] == actual_updated_tickets[index]

    # compare transactions:
    file=os.path.join(case_folder, 'kinsgton_transactions')
    assert not os.path.getsize(file)

    file=os.path.join(case_folder, 'montreal_transactions')
    assert not os.path.getsize(file)

    file=os.path.join(case_folder, 'toront_transactions')
    assert not os.path.getsize(file)
    
    # rewrite content in transaction files
    with open(os.path.join(case_folder, 'kingston_transactions'), 'r') as file:
        for i in range(1, len(kst)+1):
            index = i * -1
            file.write(kst[index])
        file.close
    with open(os.path.join(case_folder, 'montreal_transactions'), 'r') as file:
        for i in range(1, len(mtl)+1):
            index = i * -1
            file.write(mtl[index])
        file.close
    with open(os.path.join(case_folder, 'toronto_transactions'), 'r') as file:
        for i in range(1, len(trt)+1):
            index = i * -1
            file.write(trt[index])
        file.close
    
    # clean up
    os.close('updated_tickets.csv')
    os.remove('updated_tickets.csv')

    os.close('updated_account.csv')
    os.remove('updated_account.csv')
