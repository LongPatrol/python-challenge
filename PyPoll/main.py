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

#list of percentages of vote and index numbers for printing dictionary
perlist = []
indxlist =  []
for vote in votelist:
    perlist.append(round((vote/votecount)*100, 3))
    indxlist.append(votelist.index(vote))

#Election dicttionary
result = {}
result["Candidate"] = canlist
result["Percent"] = perlist
result["Votes"] = votelist

#printing results
print("Election Results")
print("------------------------------")
print(f'Total Votes: {votecount}')
print("------------------------------")
for x in indxlist:
    print(f'{result["Candidate"][x]}: {result["Percent"][x]}% ({result["Votes"][x]})')
print("------------------------------")
print(f'Winner: {winner}')
print("------------------------------")

#textfile of results
txtpath = os.path.join('Analysis', 'analysis.txt')
with open(txtpath, 'w') as txtfile:
    txtfile.write(
    "Election Results"
    "\n------------------------------"
    "\n"f'Total Votes: {votecount}'
    "\n------------------------------")
    for x in indxlist:
        txtfile.write("\n"f'{result["Candidate"][x]}: {result["Percent"][x]}% ({result["Votes"][x]})')
    txtfile.write(
    "\n------------------------------"
    "\n"f'Winner: {winner}'
    "\n------------------------------")
txtfile.close()