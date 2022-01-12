#create dict

counties = ["Arapahoe","Denver","Jefferson"]
# use boolean stmt of two equals signs to determine IF 
if counties[1] =='Denver':
        print(counties[1])
        

#practicing IN operator
if "El Paso" in counties:
        print("El Paso is in the list of counties")
else:
        print("El Paso is not in the list of counties")


#practicing AND with IN operator
if "Arapahoe" and "El Paso" in counties:
        print("Arapahoe and El Paso are in the list of counties")
else:
        print("Arapahoe or El Paso is not in the list of counties")

#practicing OR with IN operator
if "Arapahoe" or "El Paso" in counties:
        print("Arapahoe or El Paso is in the list of counties")
else:
        print("Arapahoe or El Paso is not in the list of counties")

#create a dictionary
voting_data = []

#insert keys and values into the dictionary
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})

#review the dictionary for accuracy
print(voting_data)

#insert new county and voters, EL Paso into spot 2
voting_data.insert(1,{"county":"El Paso", "registered_voters": 461149})

#review the dictionary for accuracy again
print(voting_data)

#remove Arapahoe and voters count
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})

#review the dictionary for accuracy again
print(voting_data)

#make Denver as 3rd and Jefferson as 2nd
voting_data.insert(2,{"county":"Denver", "registered_voters":463353})

#review the dictionary for accuracy again
print(voting_data)

#make Denver as 3rd and Jefferson as 2nd
voting_data.insert(1,{"county":"Jefferson", "registered_voters":432438})

#review the dictionary for accuracy again
print(voting_data)

#clean up list by removing dups - remove 2nd instance of Denver first
voting_data.pop(3)

#review the dictionary for accuracy again
print(voting_data)

#clean up list by removing dups - remove 2nd instance of Denver first
voting_data.pop(3)

#review the dictionary for accuracy again
print(voting_data)

#add Arapahoe back to dictionary
voting_data.append({"county":"Arapahoe","registered_voters":422829})

#review the dictionary for accuracy again
print(voting_data)


#For practice
for county in (counties):
    print (county)

#using a variable to keep track of range and the loop
for i in range(len(counties)):
    print(counties[i])


#Get keys or values from a dict using For loop
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.values():
        print(county)


#print keys from dict using the county key
for county in counties_dict:
        print(counties_dict[county])


#using get method for the counties to print
for county in counties_dict:
        print(counties_dict.get(county))

#printing both key and value together, whichever variable is listed first it will be the key
for county,voters in counties_dict.items():
        print(county,voters)


#the above code with additional wording, no plus signs needed
for county,voters in counties_dict.items():
        print(county,  " county has ", voters,  "registered voters.")

#printing each dict within a dict
for county_dict in voting_data:
        print(county_dict)

#only want values within the dict of dicts
for county_dict in voting_data:
        for value in county_dict.values():
                print(value)


#F string example
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#original code
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#using F print for the above code
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#multiline F strings 
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

#Multiline F strings with formatting on the numbers
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

import csv
dir (election_results.csv)


high_school_types = [{"High School": "Griffin", "Type":"District"},
                    {"High School": "Figueroa", "Type": "District"},
                    {"High School": "Wilson", "Type": "Charter"},
                    {"High School": "Wright", "Type": "Charter"}]
for High School, Type in high_school_types:
                print(high_school_types)