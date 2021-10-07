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
inputFile = os.path.join('Resources','election_data.csv')
outputfile = os.path.join("PyPoll Analysis")

#Create variables
totalVotes = 0
Candidate = [] #create unique list of candidates
CandidateVotes = {} #create dictionary of candidates votes
winCount = 0 #initialize to zero. used for winning count
winCandidate = "" #variable for the winning candidate

# open and read the csvfile
with open(inputFile) as election_data:
    csvreader = csv.reader(election_data)

    #bring in header
    header = next(csvreader)

    #create lists, index 0 for the voter ID, index 1 for the candidate selected

    #Create loop to go through election data.csv 
    
    for row in csvreader:
      totalVotes +=1

      #create unique list of candidates by checking if candidate is in the candidate list, if not then 
      #append the candidate to the list and the dictionary

      if row[2] not in Candidate:
        Candidate.append(row[2])

        #dictionary has the key and value = {"key":value} or the {candidate:number of votes}
        CandidateVotes[row[2]] = 1

      else:
          # if candidate is already in the list, then add to the candidate's votes
        CandidateVotes[row[2]] += 1

# print(CandidateVotes)
# voteOutput = f"\t{Candidate}:{votePercentage:,.2f}% \n"
output = (
  f"\n\nElection Results\n"
  f"......................\n"
  f"\tTotal Votes:{totalVotes:,}\n"
  f"\tCandidate Votes: {CandidateVotes}\n"
  
 
)      

print(output)

with open (outputfile, "w") as textfile:
  textfile.write(output)
  for candidate in CandidateVotes:
    
        # get candidate vote counts and the perecentage of votes for each candidate
    votes = CandidateVotes.get(candidate)

    votePercentage = (float(votes)/float(totalVotes))*100.00
    print(votePercentage)
    textfile.write(f"\tCandidate:{candidate}")
    textfile.write (f"\t{votePercentage:,.2f}%\n")
    
    #winning count
    if votes > winCount:
      #update to the new winning count
      winCount = votes
      #update winning candidate
      winCandidate = candidate

  textfile.write(f"\tWinning Candidate:{winCandidate}")

        





# create an output for analysis





    


