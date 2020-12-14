
# daily script functions: 
# 1. uns front end over a number of trainsactions (of your choice) for different locations, resulting different transaction files
# 2. runs back end program that merges transaction and produce new information files

# run this script by:
# sh daily.sh

# front end
chmod +x frontend/app.py
python3 frontend/app.py kingston data/user.csv data/ticket.csv