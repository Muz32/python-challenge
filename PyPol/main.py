import os
import csv
csvpath = os.path.join ("resources", "election_data.csv")


#Define the function to find the list of canditaes who received the votes
def candidate_list(electiondata):
    candidates = {}
    total_votes = 0
    for row in electiondata:
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1
        total_votes +=1
    for candidate in candidates:
        candidates[candidate] = (candidates[candidate], candidates[candidate] / total_votes * 100)
    return candidates
   
       
# Open the CSV file and define parameters of data to use in functions  
with open(csvpath) as csvfile:
    electiondata = list(csv.reader(csvfile, delimiter=','))

    #Assign the header row to variable 'header' and store the remaining rows (actual data) in the variable 'data'. 
    #This extracts the header row, and separates the data rows into a list. 
    header = electiondata[0]
    data = electiondata[1:]

    print ("Election Results\n")
    print ("--------------------------------\n")
   
   #Call the function to print the results
    Results = candidate_list(data)


    #Print total votes cast
    print(f"Total votes cast:", sum(count for count, _ in Results.values()), "\n")
    print ("--------------------------------\n")
    
#Print candidate name with their respective votes and percentage of votes
for candidate, (votes, percentage) in Results.items():
    print(f"{candidate}: {percentage:.3f}% ({votes})\n")

# Print candidate with the highest votes (winner)
print ("--------------------------------\n")
max_candidate = max(Results, key=lambda x: Results[x][0])
print(f"Winner:", max_candidate, "\n")

print ("--------------------------------\n") 


# Open a text file for writing
output_file_path = os.path.join("analysis", "PyPolResults.txt")
with open(output_file_path, "w") as PyPolResults_file:
    #Write the results to the file
    PyPolResults_file.write ("Election Results\n")
    PyPolResults_file.write ("--------------------------------\n")
    PyPolResults_file.write (f"Total votes cast:", sum(count for count, _ in Results.values()), "\n")
    PyPolResults_file.write ("--------------------------------\n")
    PyPolResults_file.write (f"{candidate}: {percentage:.3f}% ({votes})\n")
    PyPolResults_file.write ("--------------------------------\n")
    PyPolResults_file.write (f"Winner:", {max_candidate}, "\n")
    PyPolResults_file.write ("--------------------------------\n") 
   