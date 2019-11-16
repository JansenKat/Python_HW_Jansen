import csv

voter_id = []
county = []
candidate = []

#Open & parse election_data.csv
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

#Summarize candidate and votes information
for person in candidate:
    if person in unique_candatites:
        candadite_votes[unique_candatites.index(person)] +=1
    else:
        unique_candatites.append(person)
        candadite_votes.append(0)

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
lines = ["Election Results\n",
    "-------------------------\n",
    "Total Votes: " + str(votes) + "\n",
    "-------------------------\n",
    "-------------------------\n",
    "Winner: "+ winner +"\n",
    "------------------------"]

#add stats to lines
for entry in polls:
    lines.insert(-3,entry[0]+": "+str(entry[1])+"% ("+str(entry[2])+")\n")

#Create, write and read analysis file
analysis = open("Election_Analysis.txt","w+")
analysis.writelines(lines)
analysis.close()
analysis = open("Election_Analysis.txt","r+")
print(analysis.read())