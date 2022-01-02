## Import Dependencies
import csv
import os

## Import the data
# Assign variable to path of import data file (election_results.csv)
file_to_open = os.path.join("Module-3-Election-Analysis","Resources", "election_results.csv")
# Assign variable to path of export data file (election_analysis.txt)
if not os.path.exists('Module-3-Election-Analysis/Analysis'): #if the folder does not exist make on
    os.makedirs('Module-3-Election-Analysis/Analysis')
file_to_save = os.path.join("Module-3-Election-Analysis","Analysis", "election_analysis.txt")

## Open the election results as a file object(election_data)
with open(file_to_open) as election_data :
    # Read file object with reader function
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    # Print out all data without the headers from the import data file
    for row in file_reader :
        print(row)



# 1. Calculate total number of votes cast
# 2. Complie a list of candidates who received votes
# 3. Calculate total number of votes each candidate received
# 4. Calculated percentage of votes each candidate won
# 5. Determine the winner of the election based on popular vote

# Write output to text file
with open(file_to_save, "w") as txt_file :
    # Write some data to the file.
    txt_file.write("Counties in the Election")
    txt_file.write("\n------------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")

# Close the file
txt_file.close()
