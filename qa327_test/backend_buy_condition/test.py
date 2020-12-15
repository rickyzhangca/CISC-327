import tempfile
from importlib import reload
import os
import io
import sys
import unittest

path = os.path.dirname(os.path.abspath(__file__))

sys.path.append('qa327/backend2')
import backend

################################################################
# if want to force printing to console:
# pritn(something)
# assert false
################################################################

def test_b_1(capsys): # valid test for update
    helper(
        capsys=capsys,
        test_id='condition=false'
    )

def test_b_2(capsys): # invalid test for update when have invalid name input
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
    # reload(backend)

    # locate test case folder:
    case_folder = os.path.join(path, test_id)

    # prepare program parameters
    sys.argv = []

    # run the program
    in_ticket='qa327_test/backend_buy_condition/condition=false/ticket.csv'
    in_user='qa327_test/backend_buy_condition/condition=false/user.csv'
    in_transactions=['qa327_test/backend_buy_condition/condition=false/kingston_transactions.csv','qa327_test/backend_buy_condition/condition=false/montreal_transactions.csv','qa327_test/backend_buy_condition/condition=false/toronto_transactions.csv']
    out_ticket='temp/updated_tickets.csv'
    out_user='temp/updated_accounts.csv'
    out_transactions=['temp/kingston_transactions.csv','temp/montreal_transactions.csv','temp/toronto_transactions.csv']
    backend.main(in_ticket, in_user, in_transactions, out_ticket, out_user, out_transactions)

    # users -> updated
    with open(out_user, 'r') as of:
        content = of.read()
        with open(os.path.join(case_folder, 'expected_user.csv'), 'r') as exp_file_of:
            expected_content = exp_file_of.read()
            assert content == expected_content

    # tickets -> udpated
    with open(out_ticket, 'r') as of:
        content = of.read()
        with open(os.path.join(case_folder, 'expected_ticket.csv'), 'r') as exp_file_of:
            expected_content = exp_file_of.read()
            assert content == expected_content

    # transactions -> empty
    for t in out_transactions:
        with open(t, 'r') as of:
            content = of.read()
            with open(os.path.join(case_folder, 'expected_'+t), 'r') as exp_file_of:
                expected_content = exp_file_of.read()
                assert content == expected_content

