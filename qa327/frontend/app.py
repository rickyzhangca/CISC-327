import sys
import helpers


def main():
    # location of the frontend hosting
    location = sys.argv[0]

    # load the account list file and the valid ticket list file at given location
    from helpers import ResourcesHelper
    ResourcesHelper.loadUserInfo(sys.argv[1])
    ResourcesHelper.loadTicketInfo(sys.argv[2])

    print('Welcome to SeetGeek!')
    print('author @VeryUsefulGroup')

    # setting the Landing screen as the initial page.
    from sessions import LandingSession
    next_session = LandingSession()
    while next_session:
        try:
            current_session = next_session
            current_session.operate()
            next_session = current_session.routing()
            del current_session
        except Exception as e:
            print('\nUnexpected exception:')
            print(str(e))
            print('Please contact the admin for resolve, thank you!')

    # save transactions before exit.    
    from helpers import TransactionsHelper
    TransactionsHelper.saveTransactions(location)

    print('Transactions saved.')
    print()
    print('Good bye!')

main()