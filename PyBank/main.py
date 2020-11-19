# First we’ll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
csvpath = os.path.join('Resources', 'budget_data.csv')
import csv
month = 0
netTotal = 0

# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    #the differences between the profit and loss
        #Can I somehow store the difference as a new column? Or can I calculate the difference based on 
 
   #Number of months and Net total amount
    for row in csvreader:
        #Counting the total number of months (row for each month)
       month = month + 1
       netTotal = netTotal + float(row[1])
    
    print(month)
    print(netTotal)