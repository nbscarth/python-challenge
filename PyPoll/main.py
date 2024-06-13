import os
import csv

csvpath = r"D:\Scarthicus\Documents\Bootcamp\Challenges\Module_3\python-challenge\PyPoll"
election_csv = os.path.join(csvpath, "Resources", "election_data.csv")

with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csv_reader)

    ballot_count = 0
    candidate_list = []
    votes = []
    candidate_total = dict()

    for row in csv_reader:
        
        # Tallies ballots
        ballot_count += 1 

        # Candidate list
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

        # List of candidate votes
        votes.append(row[2])

    for candidate in candidate_list:

        # Counts number of votes for candidate and adding to dictionary
        vote_count = votes.count(candidate)
        candidate_total[candidate] = vote_count

    print(candidate_total)
    # Percentage of votes each candidate won
        #total won / total
    # Total number of votes each candidate won
        #
    # Winner of election based on popular vote
        #name with highest total won

    #print statements
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {ballot_count}")
    print("-----------------------------")

    print("-----------------------------")
    print("-----------------------------")