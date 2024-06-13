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
    winner_total = 0

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

        # Finds candidate with most votes
        if vote_count > winner_total:
            winner_total = vote_count
            winner = candidate

            
    # Print analysis results
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {ballot_count}")
    print("-----------------------------")
    # Individual results + print statements 
    for candidate in candidate_list:
        percent = round((candidate_total[candidate] / ballot_count) * 100, 3)
        print(f"{candidate}: {percent}% ({candidate_total[candidate]})")
    print("-----------------------------")
    print(f"Winner: {winner}")
    print("-----------------------------")

output_file = os.path.join(csvpath, "analysis", "election_results.txt")

with open(output_file, "w") as textfile:
    writer = csv.writer(textfile, delimiter=",")

    writer.writerow(["Election Results"])
    writer.writerow(["-----------------------------"])
    writer.writerow([f"Total Votes: {ballot_count}"])
    writer.writerow(["-----------------------------"])
    for candidate in candidate_list:
        percent = round((candidate_total[candidate] / ballot_count) * 100, 3)
        writer.writerow([f"{candidate}: {percent}% ({candidate_total[candidate]})"])
    writer.writerow(["-----------------------------"])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["-----------------------------"])
