# Election-Analysis Project


## Overview
The Colorado board of elections has requested analysis and results from the voting data provided for three of their counties. Tom was the project manager providing the data and instructions on which pieces of information were crucial for this project. The following is a list of the required items.  With the challenge, additional analysis was requested and is outlined below for data at the county level.   

*Candidate Level Requests
* Total number of votes cast
* A complete list of candidates who received votes
* Total number of votes each candidate received
* Percentage of votes each candidate won
* The winner of the election based on popular vote

*County Level Requests
* The voter turnout for each county
* The percentage of votes from each county out of the total count
* The county with the highest turnout

## Election-Audit Results
The three counties had three candidates in the race for election. The results of this election are provided at the candidate and county level.  The results are viewable within the text file in this repo and are also screen printed in this document.

A detailed summary of the election results is as follows:

### 369,711 Total Votes

County Level Results:

* Denver County
  * 306,055 total votes
  * 82.8% of the total vote count

* Jefferson County
  * 38,855 total votes
  * 10.5% of the total vote count

* Arapahoe County
  * 24,801 total votes
  * 6.7% of the total vote count

## County with Largest Voter Turnout: DENVER

Candidate Level Results:

* Charles Casper Stockham
  * 85,213 total votes
  * 23.0% of the total vote count

* Diana DeGette
  * 272,892 total votes
  * 73.8% of the total vote count

* Raymon Anthony Doane
  * 11,606 total votes
  * 3.1% of the total vote count


# **Winner of this Election: DIANNA DEGETTE**




![4F345B2C-08DF-400C-A06A-6E95C043F491](https://user-images.githubusercontent.com/96222437/149555326-abf28491-6094-4b26-98b7-c68fc2160d2a.jpeg)



## Election-Audit Summary

The Colorado board of elections can continue to obtain voting results from these three counties for future elections by running these scripts.  The board can also find these scripts helpful in other elections by making modifications to the existing code base to allow for further analysis or different analysis, as needed. 

An enhancement that can be done to provide further use of these scripts is to add code to track and count the *method* of voting by voters in the area.  A variable can be added to provide results for the following categories: voting in person vs advanced voters vs mail in voters.  The variable would be similar to the county or candidate variable and could be added to a new For loop to count the method of voting by row.  This data would have to be gathered and provided within the datasheet, as well.     

A second use for the scripts could be to perform this analysis at a different level of elections.  The code can be modified and utilized for city elections by updating a few lines of the code. The county references will be replaced with city and the candidate references will remain unchanged so that the results can produce at that level. 
