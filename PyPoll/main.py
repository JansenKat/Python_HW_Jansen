import os
import csv

voter_id = []
county = []
candadite = []

#Open & parse election_data.csv
with open(os.path.join('Resources','election_data.csv'),'r') as textfile:
    election_data = csv.DictReader(textfile)
    for row in election_data:
        voter_id.append(row['Voter ID'])
        county.append(row['County'])
        candadite.append(row['Candidate'].strip())

total_votes = len(voter_id)

#Summarize candidate and votes information
unique_candatites = []
unique_candatites = list(set(candadite))
candadite_votes = []
candadite_votes = [candadite.count(person) for person in unique_candatites]

#Calculate percentage
candidate_percentage = []
for votes in candadite_votes:
    candidate_percentage.append(round(votes/total_votes*100,3))

#Identify winner
winner_index = candadite_votes.index(max(candadite_votes))
winner = unique_candatites[winner_index]

#Compile poll statistics
polls = []
for i in range(len(unique_candatites)):
    entry = [unique_candatites[i],candidate_percentage[i],candadite_votes[i]]
    polls.append(entry)

#Establishing format in list
lines = ['Election Results\n',
    '-------------------------\n',
    f'Total Votes: {votes}\n',
    '-------------------------\n',
    '-------------------------\n',
    f'Winner: {winner}\n',
    '-------------------------']

#add stats to lines
for entry in polls:
    lines.insert(-3,f'{entry[0]}: {entry[1]}% ({entry[2]})\n')

#Create, write and read analysis file
analysis = open('Election_Analysis.txt','w+')
analysis.writelines(lines)
analysis.close()
analysis = open('Election_Analysis.txt','r+')
print(analysis.read())