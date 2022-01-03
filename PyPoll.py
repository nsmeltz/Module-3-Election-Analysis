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
candidate_options = [] #list [1,2,3]
candidate_votes = {} #dictionary {key:value}
winning_candidate = "" #empty string
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
        total_votes += 1 #total_votes = total_votes + 1

        #Add candidate name to list if it is not already in the list
        candidate_name = row[2]
        if candidate_name not in candidate_options :
            # Add candidate name to list
            candidate_options.append(candidate_name)
            # 3. Calculate total number of votes each candidate received
            candidate_votes[candidate_name] = 0
        # Add a vote to candidate's count
        candidate_votes[candidate_name] += 1

#Print results to text file & terminal
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)    

    ## Print Outputs to Terminal
    # print(f" Total Number of Votes = {total_votes} ")
    # print(f"Candidate Options: {candidate_options}")
    # print(f"Candidate Votes: {candidate_votes}")

    # 4. Calculated percentage of votes each candidate won & who won the election
    for candidate_name in candidate_votes :
        
        # retieve votes each candidate got
        votes = candidate_votes[candidate_name]
        
        #calcualte percentage
        vote_percentage = float(votes) / float(total_votes) *100
        
        #print to name, %, and votes to terminal    
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
        
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
        f"Winner = {winning_candidate}\n"
        f"Winning Vote Count = {winning_count:,} votes\n"
        f"Winning Percentage = {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
