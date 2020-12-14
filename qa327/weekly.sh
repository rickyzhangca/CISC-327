
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
    cat weekly/daily${i}/daily_kingston.txt | python3 frontend/app.py kingston data/user.csv data/ticket.csv
    cat weekly/daily${i}/daily_toronto.txt | python3 frontend/app.py toronto data/user.csv data/ticket.csv
    cat weekly/daily${i}/daily_montreal.txt | python3 frontend/app.py montreal data/user.csv data/ticket.csv

    # back end 
    chmod +x backend2/backend.py
    python3 backend2/backend.py

    cp data/user.csv weekly_data/daily${i}/
    cp data/ticket.csv weekly_data/daily${i}/

    cp data/kingston_transactions.csv weekly_data/daily${i}/
    cp data/montreal_transactions.csv weekly_data/daily${i}/
    cp data/toronto_transactions.csv weekly_data/daily${i}/

done
