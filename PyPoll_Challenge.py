import pandas as pd
import csv
import os
import numpy as np

#File Paths
file = r'C:\Users\mattg\Desktop\Columbia\Module 3\csv Files\election_results.csv'
file_to_save = r'C:\Users\mattg\Desktop\Columbia\Module 3\txt Files\electionAnalysis.txt'

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_dict = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = ''
voter_turnout = 0

df = pd.read_csv(file)

        
total_votes = len(df)
candidate_options = pd.Series(df['Candidate']).unique()
candidate_options = candidate_options.tolist()

county_list = pd.Series(df['County']).unique()
county_list = county_list.tolist()

candidate_votes = df['Candidate'].value_counts()
candidate_votes = candidate_votes.to_dict()

county_dict = df['County'].value_counts()
county_dict = county_dict.to_dict() 
county_dict
# Print the final vote count (to terminal)

with open(file_to_save, "w") as txt_file:
    election_results = (
      f"\nElection Results\n"
       f"-------------------------\n"
      f"Total Votes: {total_votes:,}\n"
     f"-------------------------\n"
       f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)
    
with open(file_to_save, "a") as txt_file:    
    for county in county_dict:
        votes = county_dict.get(county)
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
        f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        txt_file.write(county_results)

#Couldn't figure out the if statement placeholder code Works Cited: https://www.codegrepper.com/code-examples/python/python+return+key+with+largest+value
with open(file_to_save, "a") as txt_file:
    max_key = max(county_dict, key=county_dict.get)
    largest_county_results = (
    f"-------------------------\n"
    f"Largest County Turnout: {max_key}\n"
    f"-------------------------\n")
    print(largest_county_results)
    txt_file.write(largest_county_results)

with open(file_to_save, "a") as txt_file:
    for candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
           f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    # Save the winning candidate's name to the text file
    #txt_file.write(winning_candidate_summary)





    
    


    
    

        

