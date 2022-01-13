

# Assign a variable for the file to load and the path.
#file_to_load = '/Users/jerrilynmorales/Downloads/Python /Resources/election_results.csv'



# Open the election results and read the file.
#election_data = open(file_to_load,'r')

#To do: perform analysis.

#Close the file.
#election_data.close()

#redo code with WITH stmt for opening and reading
#version 2
#with open(file_to_load) as election_data:

    #to do: peform analysis.
    #print(election_data)


#import csv
#import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
     #print(election_data)


# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")


# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.

file_to_load = os.path.join("/Users/jerrilynmorales/Downloads/Python/PyPoll_Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Adding total vote counter
total_votes = 0 

#Candidate list
candidate_options = []

#dictionary for candidate votes
candidate_votes = {}

#variable for winning candidate
winning_candidate = ""

#variable for winning count
winning_count = 0

#variable for winning_percentage
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read a the header row
    headers = next(file_reader)
    #and print header row
    #print(headers)

    #Print each row in the CSV file.
    for row in file_reader:
        #add to the total vote count.
        total_votes += 1
        #print candidate name 
        candidate_name = row[2]
        

        #Check if candidate name in the list, so we only add it once.
        if candidate_name not in candidate_options:
             #add to the list of candidates   
            candidate_options.append(candidate_name)
            #begin tracking the candidate's vote count.
            candidate_votes[candidate_name] = 0
        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        
    
    #Determining % of total votes for each candidate
    # 1. iterate through candidate list
    for candidate_name in candidate_votes:
        #2 Retrieve vote count
        votes = candidate_votes[candidate_name]
        vote_percentage = float (votes) / float (total_votes) * 100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        
    #setting values for winning items
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #set winning count and winning % to new values
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    #print to the terminal the winning candidates
    winning_candidate_summary = (
        f".........................\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

print(winning_candidate_summary)
    
        
    #To do: print out the winning candidate, vote count and percentage to
#   terminal.
    
        #print(f"{candidate_name} :  received  {vote_percentage}% of the total votes.")
       
#Print list of candidates
#print(candidate_votes)


        
