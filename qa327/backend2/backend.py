
import csv
import sys

# add 'qa327' to all paths if you are to run this file directly

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
            match_tickets = [t for t in tickets if t[0] == transaction[2]]

            if len(match_tickets) == 1: # sell exiting ticket
                ticket_index = tickets.index(match_tickets[0])
                tickets[ticket_index][2] = str(int(tickets[ticket_index][2]) + int(transaction[4]))
            elif len(match_tickets) == 0: # sell new ticket
                tickets.append([transaction[2],transaction[3],transaction[4],transaction[1],transaction[-1]])    
            else: # multiple matching tickets
                print('error')
        except:
            print('error')    

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

def main(in_ticket='data/ticket.csv', 
        in_user='data/user.csv', 
        in_transactions=['data/kingston_transactions.csv','data/montreal_transactions.csv','data/toronto_transactions.csv'],
        out_ticket='data/updated_tickets.csv', 
        out_user='data/updated_accounts.csv',
        out_transactions=['data/kingston_transactions.csv','data/montreal_transactions.csv','data/toronto_transactions.csv']):
    
    import os
    os.chdir("..")
    # get tickets and users
    tickets, users = get_data(in_ticket,in_user)

    # get transactions, from fixed paths or arguments
    # transactions = sys.argv[1:]
    # transactions = get_transactions(['qa327/data/test_transactions.csv'])
    transactions = get_transactions(in_transactions)

    # process transactions
    process(tickets, users, transactions)

    # save new tickets and users, to new file, or replace the previous file
    # save('qa327/data/ticket.csv',tickets)
    # save('qa327/data/user.csv',users)
    save(out_ticket,tickets)
    save(out_user,users)

    # empty transanction files
    for t in out_transactions:
        save(t,[])

if __name__ == '__main__':
    main()