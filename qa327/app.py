import sys
import os

def main():
    
    next_session = LandingSession()
    while next_session:
        current_session = next_session
        current_session.operate()
        next_session = current_session.routing()
        del current_session
        
main()