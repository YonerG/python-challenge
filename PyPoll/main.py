"""
The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote

Calculate the total votes and votes per candidate first because it will make calculations percentage 
and winner easier

"""



#import the csv

import csv
import os

#read csv file
inputFile = os.path.join("election_data.csv")

#Create variables
totalVotes = 0

# open and read the csvfile
with open(inputFile) as election_data:
    csvreader = csv.reader(election_data)

    #bring in header
    header = next(csvreader)
    


