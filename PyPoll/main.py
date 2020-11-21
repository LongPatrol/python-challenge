import os
csvpath = os.path.join('Resources', 'election_data.csv')
import csv


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')    
    csv_header = next(csvreader)

    votecount = 1
    canlist = []
    firstline = next(csvreader)
    candidate = str(firstline[2])
    canlist.append(candidate)
  
 
    for row in csvreader:
        votecount = votecount + 1
        can2 = str(row[2])
        if can2 not in canlist:
            canlist.append(can2)
            

    #print(row[2])
    print(canlist)   
    print(votecount)