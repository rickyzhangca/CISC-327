
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
    chmod +x frontend/app.py
    cat weekly/daily${i}/daily_kingston.txt | python3 frontend/app.py kingston data/updated_accounts.csv data/updated_tickets.csv
    cat weekly/daily${i}/daily_toronto.txt | python3 frontend/app.py toronto data/updated_accounts.csv data/updated_tickets.csv
    cat weekly/daily${i}/daily_montreal.txt | python3 frontend/app.py montreal data/updated_accounts.csv data/updated_tickets.csv

    # back end 
    python3 -c 'import backend; backend.main()'
done
