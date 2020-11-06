import sys

import sessions
import helpers

def main():

    location = sys.argv[1]

    helpers.ResourcesHelper.loadUserInfo(sys.argv[2])
    helpers.ResourcesHelper.loadTicketInfo(sys.argv[3])

    print('Welcome to SeetGeek!')
    print('author @VeryUsefulGroup')

    next_session = sessions.LandingSession()
    while next_session:
        current_session = next_session
        current_session.operate()
        next_session = current_session.routing()
        del current_session
    
    helpers.TransactionsHelper.saveTransactions(location)
    
    print('Transactions saved.')
    print()
    print('Good bye!')