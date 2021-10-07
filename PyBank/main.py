"""
The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in profits (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)


"""

import os 
import csv


fileload =os.path.join('PyBank','Resources', 'budget_data.csv')
outputfile = os.path.join("Pybank Analysis.txt")
#The total number of months in the dataset
totalMonths = 0
#Net total of the profit/losses
NetTotal = 0
#Monthly changes in profit/losses, create a list to hold the changes
MonthlyChanges = [] #initialize the list for monthly changes
months = []      #initialize the list of months

with open(fileload) as budget_data:
    csvreader = csv.reader(budget_data)
    header = next(csvreader) # this reads in the header
    # move to the first row to start reading the first profit/loss value in the dataset
    firstrow = next(csvreader)

        
     #increment the count of the total months
    totalMonths += 1
    #calculate the NetTotal
    NetTotal += float(firstrow[1])
       #establish previous profit
    previousprofit = firstrow[1]   
   
    for row in csvreader:
    #increment the count of the total months
      totalMonths += 1
    #calculate the NetTotal
      NetTotal += float(float(row[1]))

    #calculate the net change inside loop
      NetChange = float(float(row[1]) - float(previousprofit))
      # add changes to the monthly change list
      MonthlyChanges.append(NetChange)

      # first month that change occured
      months.append(row[0])

      #update the previous revenue
      previousprofit = (row[1])

#Calculate the average net change per month
averageChange = sum(MonthlyChanges)/ len(MonthlyChanges)

greatestIncrease = [months[0], MonthlyChanges[0]] # the month and value of greatest increase
greatestDecrease = [months[0], MonthlyChanges[0]] # the month and the value of greatest decrease

for m in range(len(MonthlyChanges)):

  #calculate the greatest increase 

 if(MonthlyChanges[m] > greatestIncrease[1]):
   greatestIncrease[1] = MonthlyChanges[m]

   #update the month when the new value for greatest increase changes
   greatestIncrease[0] = months[m]

  #calculate the greatest decrease
 if(MonthlyChanges[m] < greatestDecrease[1]):
   greatestDecrease[1] = MonthlyChanges[m]
   
   
   #update the month when the new value for greatest increase changes
   greatestDecrease[0] = months[m]

   



    
output = (
  f"\nPyBank Analysis \n"
  f"--------------------\n"
  f"\tTotal Months: {totalMonths}\n"
  f"\tNet Total: ${NetTotal:,.2f}\n"
  f"\tAverage Change Per Month: ${averageChange:,.2f}\n"
  f"\tGreatest Increase: {greatestIncrease[0]} Amount ${greatestIncrease[1]:,.2f}\n"
  f"\tGreatest Decrease: {greatestDecrease[0]} Amount ${greatestDecrease[1]:,.2f}\n"
  
)

print(output)

with open(outputfile, "w") as textfile:
    textfile.write(output)







