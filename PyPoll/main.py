import os
csvpath = os.path.join('Resources', 'election_data.csv')
import csv


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')    
    csv_header = next(csvreader)

    votecount = 1
    canlist = []
    votelist = [1]
    firstline = next(csvreader)
    candidate = str(firstline[2])
    canlist.append(candidate)
  
 
    for row in csvreader:
        votecount = votecount + 1
        can2 = str(row[2])
        if can2 not in canlist:
            canlist.append(can2)
            votelist.append(1)

        #votes for each candidate
        elif can2 in canlist:
           votelist[canlist.index(can2)] = votelist[canlist.index(can2)] + 1
     
    winner = canlist[votelist.index(max(votelist))]
    print(winner)
    print(canlist)   
    print(votecount)
    print(votelist)