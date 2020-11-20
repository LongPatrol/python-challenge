import os
csvpath = os.path.join('Resources', 'budget_data.csv')
import csv


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #count the month from the first row, since we're not including the first row in the loop
    month = 1
    netTotal = 0
    #put our differences in a this list
    difflist = []

    firstline = next(csvreader)
    maxdiff = 0.0
    mindiff = 0.0
    maxmonth = 'month'
    minmonth = 'month'
 
    for row in csvreader:
        #Counting the total number of months (row for each month)
       month = month + 1
       netTotal = netTotal + float(row[1]) 
       difference = float(row[1]) - float(firstline[1])

        #max difference and the month of the max difference
       if difference > maxdiff:
           maxdiff = difference
           maxmonth = str(row[0])

        #mmin difference and the month of the mmin difference
       if difference < mindiff:
            mindiff = difference
            minmonth = str(row[0])
      
       difflist.append(difference)
       firstline = row 
    netTotal = round(netTotal + float(firstline[1]))

    #defining average function
    def average(numlist):
        count = len(numlist)
        total = 0.00
        for number in numlist:
            total += number
        return total/count
    avgdiff = round(average(difflist), 2)

    #diffmax = round(max(difflist))
    #diffmin = round(min(difflist))

    #printing out what we want
    #!!!! need to add the whole sentence structure via fstr
    print(month)
    print(netTotal)
    print(avgdiff)
    print(mindiff)
    print(maxdiff)
    print(maxmonth)
    print(minmonth)
    #print(diffmax)
    #print(diffmin)
  