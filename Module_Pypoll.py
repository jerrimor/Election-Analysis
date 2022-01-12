# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of canddiates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote



# Open the election results and read the file.


# To do: perform analysis.

# Close the file.



import csv
import os

# Assign a variable for the file to load and the path.
with open ("/Users/jerrilynmorales/Downloads/Python /Resources/election_results.csv") as file_to_load:
    with open(file_to_load) as election_data:
        #To do; perform analysis
        print(election_data)








# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join( "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")


# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

# Close the file
