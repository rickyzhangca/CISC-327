user_info = {}
ticket_info = {}

user_file_path = 'qa327/data/user.csv'
ticket_file_path = 'qa327/data/ticket.csv'

class ResourcesHelper:

    @staticmethod
    def setUserFilePath(file_path):
        user_file_path = user_file

    @staticmethod
    def setTicketFilePath(file_path):
        ticket_file_path = file_path        

    @staticmethod
    def loadUserInfo():
        user_file = open(user_file_path, 'r').read().split('\n')
        for i in user_file:
            record = i.split(', ')
            user_info[record[1]] = {
                'email': record[0],
                'password': record[2],
                'balence': float(record[3]),
            }
    
    @staticmethod
    def loadTicketInfo():        
        ticket_file = open(ticket_file_path, 'r').read().split('\n')
        for i in ticket_file:
            record = i.split(', ')
            ticket_info[record[0]] = {
                'price': float(record[1]),
                'number': int(record[2]),
                'email': record[3],
            }

    @staticmethod
    def getUserInfo():
        return user_info

    
    @staticmethod
    def getTicketInfo():
        return ticket_info