user_info = {}
ticket_info = {}

user_file = open('d:/2020_Fall/CMPE 327/project/CISC-327/qa327/user.csv', 'r').read().split('\n')
ticket_file = open('d:/2020_Fall/CMPE 327/project/CISC-327/qa327/ticket.csv', 'r').read().split('\n')

class ResourcesHelper:

    @staticmethod
    def loadUserInfo():
        for i in user_file:
            record = i.split(', ')
            user_info[record[1]] = {
                'email': record[0],
                'password': record[2],
                'balence': float(record[3]),
            }
    
    @staticmethod
    def loadTicketInfo():
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