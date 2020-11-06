import sys

import sessions
import helpers

def main():

    # location of the frontend hosting
    location = sys.argv[1]

    # load the account list file and the valid ticket list file at given location
    helpers.ResourcesHelper.loadUserInfo(sys.argv[2])
    helpers.ResourcesHelper.loadTicketInfo(sys.argv[3])

    print('Welcome to SeetGeek!')
    print('author @VeryUsefulGroup')

    # setting the Landing screen as the initial page.
    next_session = sessions.LandingSession()
    while next_session:
        current_session = next_session
        current_session.operate()
        next_session = current_session.routing()
        del current_session

    # save transactions before exit.    
    helpers.TransactionsHelper.saveTransactions(location)

    print('Transactions saved.')
    print()
    print('Good bye!')