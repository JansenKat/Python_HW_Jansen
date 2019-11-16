import csv

voter_id = []
county = []
candidate = []

#Open election_data.csv
with open("Resources/election_data.csv","r") as textfile:
    election_data = csv.reader(textfile)
    header = next(election_data)
    for row in election_data:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2].strip())

total_votes = sum(1 for row in voter_id)

unique_candatites = []
candadite_votes = []
polls = [unique_candatites,candadite_votes]

for person in candidate:
    if person in unique_candatites:
        candadite_votes[unique_candatites.index(person)] +=1
    else:
        unique_candatites.append(person)
        candadite_votes.append(0)

candidate_percentage = []
for votes in candadite_votes:
    candidate_percentage.append(round(votes/total_votes*100,3))
polls.append(candidate_percentage)
print(polls)

#Create analysis file
#analysis = open("Election_Analysis.txt","w+")

Lines = ["Election Results\n","-------------------------\n",
    "Total Votes: " + str(votes) + "\n" 
    +"-------------------------\n",
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
    "-------------------------\n",
    "Winner: "+ "'------------------------"]