
# weekly script functions: 
# 1. runs the Daily script five separate times
# 2. empty user/ticket information file

# run this script by:
# sh weekly.sh

> data/user.csv
> data/ticket.csv

for i in $(seq 1 5);
do
    # front end
    chmod +x frontend
    cat weekly/daily${i}/daily_kingston.txt | python3 frontend kingston data/updated_accounts.csv data/updated_tickets.csv
    cat weekly/daily${i}/daily_toronto.txt | python3 frontend toronto data/updated_accounts.csv data/updated_tickets.csv
    cat weekly/daily${i}/daily_montreal.txt | python3 frontend montreal data/updated_accounts.csv data/updated_tickets.csv
    
    # store transaction file into weekly data
    cp data/kingston_transactions.csv weekly_data/daily${i}/
    cp data/montreal_transactions.csv weekly_data/daily${i}/
    cp data/toronto_transactions.csv weekly_data/daily${i}/
    
    # back end 
    python3 backend

    # store updated file into weekly dara
    cp data/updated_accounts.csv weekly_data/daily${i}/
    cp data/updated_tickets.csv weekly_data/daily${i}/

done
