
import csv
import sys

'''
csv -> list, by row
'''
def read(file):
    results = []
    with open(file, newline='') as inputfile:
        for row in csv.reader(inputfile):
            row = [r.strip() for r in row]
            results.append(row)
    return results

'''
sort transactions files and merge the transactions
'''
def get_transactions(files):
    files.sort()
    transactions = []
    for i in range(len(files)): transactions.append(read(files[i]))
    return sum(transactions, [])

'''
get tickets + users
'''
def get_data(file_tickets, file_users):
    return read(file_tickets), read(file_users)

'''
list -> csv
'''
def save(file, data):
    with open(file, 'w') as outputfile:
        for row in data:
            outputfile.write(', '.join(row) + '\n')

'''
process a transaction
'''
def process(tickets, users, transactions):

    '''
    register: add new user to users
    '''
    def register(transaction):
        if transaction[2] in [u[0] for u in users]:
            print('error')
            return
        users.append([transaction[2],transaction[1],transaction[3],transaction[4]])

    '''
    buy: take user's balance and decrease ticket quantity, when user can afford and there are tickets left
    '''
    def buy(transaction):
        try:
            user_index = users.index([u for u in users if u[1] == transaction[1]][0])
            ticket_index = tickets.index([t for t in tickets if t[0] == transaction[2]][0])
            cost = float(transaction[3]) * float(int(transaction[4])) * (1 + 0.35 + 0.05)

            if float(users[user_index][3]) >= cost and int(tickets[ticket_index][2]) >= int(transaction[4]):
                users[user_index][3] = str(float(users[user_index][3]) - cost)
                tickets[ticket_index][2] = str(int(tickets[ticket_index][2]) - int(transaction[4]))
        except:
            print('error')     

    '''
    sell: increase ticket quantity, or add new ticket
    '''
    def sell(transaction):
        try:
            ticket_index = tickets.index([t for t in tickets if t[0] == transaction[2]][0])
            tickets[ticket_index][2] = str(int(tickets[ticket_index][2]) + int(transaction[4]))
        except:
            tickets.append([transaction[2],transaction[3],transaction[4],transaction[1],transaction[-1]])    

    '''
    update: directly update ticket information
    '''
    def update(transaction):
        try:
            ticket_index = tickets.index([t for t in tickets if t[0] == transaction[2]][0])
            tickets[ticket_index][1] = str(int(transaction[3]))
            tickets[ticket_index][2] = str(int(transaction[4]))
            tickets[ticket_index][3] = transaction[1]
            tickets[ticket_index][-1] = transaction[-1]
        except:
            print('error')

    '''
    transaction indicates what action to perform
    '''
    for i in range(len(transactions)):
        if transactions[i][0] == 'register': 
            register(transactions[i])
        elif transactions[i][0] == 'buy': 
            buy(transactions[i])
        elif transactions[i][0] == 'sell': 
            sell(transactions[i])
        elif transactions[i][0] == 'update': 
            update(transactions[i])

# get tickets and users
tickets, users = get_data('qa327/data/ticket.csv','qa327/data/user.csv')

# get transactions, from fixed paths or arguments
# transactions = sys.argv[1:]
transactions = get_transactions(['qa327/data/kingston_transactions.csv','qa327/data/montreal_transactions.csv','qa327/data/toronto_transactions.csv'])

# process transactions
process(tickets, users, transactions)

# save new tickets and users, to new file, or replace the previous file
# save('qa327/data/ticket.csv',tickets)
# save('qa327/data/user.csv',users)
save('qa327/data/new_ticket.csv',tickets)
save('qa327/data/new_user.csv',users)