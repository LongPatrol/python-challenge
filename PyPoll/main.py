import os
csvpath = os.path.join('Resources', 'election_data.csv')
import csv


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')    
    csv_header = next(csvreader)

    votecount = 0

    for row in csvfile:
        votecount = votecount + 1
    print(votecount)