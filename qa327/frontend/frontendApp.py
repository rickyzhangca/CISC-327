import sys

import sessions
import helpers

def main():

    region = sys.argv[1]

    helpers.ResourcesHelper.loadUserInfo(sys.argv[2])
    helpers.ResourcesHelper.loadTicketInfo(sys.argv[3])

    next_session = sessions.LandingSession()
    while next_session:
        current_session = next_session
        current_session.operate()
        next_session = current_session.routing()
        del current_session
        