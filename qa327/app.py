import sys
import os
import frontend.sessions as sessions

def main():
    
    next_session = sessions.LandingSession()
    while next_session:
        current_session = next_session
        current_session.operate()
        next_session = current_session.routing()
        del current_session
        
main()