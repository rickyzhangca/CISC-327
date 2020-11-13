import sys


def main():
    # location of the frontend hosting
    location = sys.argv[-3]

    # load the account list file and the valid ticket list file at given location
    import helpers
    helpers.ResourcesHelper.loadUserInfo(sys.argv[-2])
    helpers.ResourcesHelper.loadTicketInfo(sys.argv[-1])

    print('Welcome to SeetGeek!')
    print('author @VeryUsefulGroup')

    # setting the Landing screen as the initial page.
    import sessions
    next_session = sessions.LandingSession()
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
    helpers.TransactionsHelper.saveTransactions(location)

    print('Transactions saved.')
    print()
    print('Good bye!')

main()