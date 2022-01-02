## Import Dependencies
import csv
import os

# Assign variable to path of import data file (election_results.csv)
file_to_open = os.path.join("Module-3-Election-Analysis","Resources", "election_results.csv")
# Assign variable to path of export data file (election_analysis.txt)
if not os.path.exists('Module-3-Election-Analysis/Analysis'): #if the folder does not exist make on
    os.makedirs('Module-3-Election-Analysis/Analysis')
file_to_save = os.path.join("Module-3-Election-Analysis","Analysis", "election_analysis.txt")

# Initialize Variables
total_votes = 0 
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_open) as election_data :
    # Read file object with reader function
    file_reader = csv.reader(election_data)

    # Print out all data starting at after headers from the import data CSV
    headers = next(file_reader)
    for row in file_reader :
        #Add up total vote count
        total_votes += 1 

        #Add candidate name to list if it is not already in the list
        candidate_name = row[2]
        if candidate_name not in candidate_options :
            candidate_options.append(candidate_name)
            # 3. Calculate total number of votes each candidate received
            candidate_votes[candidate_name] = 0
            # Add a vote to candidate's count
        candidate_votes[candidate_name] += 1

# Print Outputs to Terminal
print(f" Total Number of Votes = {total_votes} ")
print(f"Candidate Options: {candidate_options}")
#print(f"Candidate Votes: {candidate_votes}")

# 4. Calculated percentage of votes each candidate won & who won the election

for candidate_name in candidate_votes :
    votes = candidate_votes[candidate_name] #number of votes each candidate got
    vote_percentage = float(votes) / float(total_votes) *100
    
    #print(f" {candidate_name} recieved {vote_percentage:.1f}% of the vote.")
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
     # If true then set winning_count = votes and winning_percent = vote_percentage.
     winning_count = votes
     winning_percentage = vote_percentage
     #Set the winning_candidate equal to the candidate's name.
     winning_candidate = candidate_name


#Print winning candidate, vote count and percentage to terminal.

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


# Write output to text file
with open(file_to_save, "w") as txt_file :
    # Write some data to the file.
    txt_file.write("Counties in the Election")
    txt_file.write("\n------------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")

# Close the file
txt_file.close()
