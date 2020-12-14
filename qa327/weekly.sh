
# weekly script functions: 
# 1. runs the Daily script five separate times
# 2. empty user/ticket information file

# run this script by:
# sh weekly.sh

> user.csv
> ticket.csv

for i in $(seq 1 5);
do
    sh daily.sh
done