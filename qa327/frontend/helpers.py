user_info = {}
ticket_info = {}

location = None

transactions = []

class ResourcesHelper:

    @staticmethod
    def loadUserInfo(user_file_path):
        user_file = open(user_file_path, 'r').read().split('\n')
        for i in user_file:
            record = i.split(', ')
            user_info[record[1]] = {
                'email': record[0],
                'password': record[2],
                'balence': float(record[3]),
            }
    
    @staticmethod
    def loadTicketInfo(ticket_file_path):        
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


class TransactionsHelper:

    @staticmethod
    def saveTransactions(location):
        transaction_file = open(location + '_transactions.csv', 'w+')
        for i in transactions:
            transaction_file.write(i)
        transaction_file.close()

    @staticmethod
    def newUserTransaction(transaction_name, user_name, user_email, user_password, balance)
        transactions.append(transaction_name + ', ' + user_name + ', ' + user_email + ', ' + user_password + ', ' + balance)

    @staticmethod
    def newTicketTransaction(transaction_name, user_name, ticket_name, ticket_price, quantity)
        transactions.append(transaction_name + ', ' + user_name + ', ' + ticket_name + ', ' + ticket_price + ', ' + quantity)