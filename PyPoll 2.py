

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
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    print(election_data)
    # To do: read and analyze the data here.