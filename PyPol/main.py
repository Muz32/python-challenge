import os
import csv

csvpath = os.path.join("resources", "election_data.csv")

# Define the function to find the list of candidates who received the votes
def candidate_list(electiondata):
    candidates = {}
    total_votes = 0
    for row in electiondata:
        candidate_name = row[2]
        candidates[candidate_name] = candidates.get(candidate_name, 0) + 1
        total_votes += 1
    return {candidate: (votes, votes / total_votes * 100) for candidate, votes in candidates.items()}

# Open the CSV file and extract data
with open(csvpath) as csvfile:
    electiondata = list(csv.reader(csvfile, delimiter=','))
    header, data = electiondata[0], electiondata[1:]

# Print results
print("Election Results\n--------------------------\n")

#Call the function to print the results
results = candidate_list(data)

total_votes = sum(votes for votes, _ in results.values())
print(f"Total votes: {total_votes}\n\n--------------------------\n\n")

# Print candidate names with their respective votes and percentage of votes
for candidate, (votes, percentage) in results.items():
    print(f"{candidate}: {percentage:.3f}% ({votes})\n")

# Print the winner
    winner = max(results, key=lambda x: results[x][0])
print(f"--------------------------\n\nWinner: {winner}\n\n--------------------------")

# Write results to a text file
    
output_file_path = os.path.join("analysis", "PyPolResults.txt")

with open(output_file_path, "w") as PyPolResults_file:
    PyPolResults_file.write("Election Results\n\n--------------------------\n\n")
    PyPolResults_file.write(f"Total Votes: {total_votes}\n\n--------------------------\n\n")
       
    for candidate, (votes, percentage) in results.items():
        PyPolResults_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n\n")
    
    PyPolResults_file.write(f"--------------------------\n\nWinner: {winner}\n\n--------------------------")
