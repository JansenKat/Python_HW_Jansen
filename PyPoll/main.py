#Define Lists
voter = []
county = []
candidate = []


#Open election_data.csv
with open("Resources/election_data.csv","r") as election_data:
    for row in election_data:
        row = row.strip().split(",")
        voter.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

votes = sum(1 for row in voter)
#Create analysis file
analysis = open("Election_Analysis.txt","w+")

Lines = ["Election Results\n","-------------------------\n",
    "Total Votes: " + str(votes) + "\n" 
    +"-------------------------\n",
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
    "-------------------------\n",
    "Winner: "+ "'------------------------"]