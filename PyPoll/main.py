import os
import csv
import pprint

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
candidate_percentage = [round(votes/total_votes*100,3) for votes in candadite_votes]

#Identify winner
winner_index = candadite_votes.index(max(candadite_votes))
winner = unique_candatites[winner_index]

#Compile poll statistics
keys = ['Candadite','Percentage','Votes']
polls = [{keys[0]:unique_candatites, keys[1]:candidate_percentage, keys[2]:candadite_votes}
        for unique_candatites, candidate_percentage, candadite_votes in zip(unique_candatites, candidate_percentage, candadite_votes)
       ]
polls = sorted(polls, key = lambda i: int(i['Votes']),reverse=True)


#Establishing format in list
lines = ['Election Results\n',
    '-------------------------\n',
    f'Total Votes: {total_votes}\n',
    '-------------------------\n'
    ]

#add stats to lines]
for entry in polls:
    lines.append(entry['Candadite']+ ': '+str(entry['Percentage'])+'% ('+str(entry['Votes'])+')\n')

winner_list = ['-------------------------\n',
            f'Winner: {winner}\n',
            '-------------------------']

lines = lines + winner_list

#Create, write and read analysis file
analysis = open('Election_Analysis.txt','w+')
analysis.writelines(lines)
analysis.close()
analysis = open('Election_Analysis.txt','r+')
print(analysis.read())