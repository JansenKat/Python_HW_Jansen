import os
import csv

date = []
profit_loss = []
change = []

#Open & parse budget_data
with open(os.path.join('Resources','budget_data.csv'), 'r') as csvfile:
    budget_data = csv.reader(csvfile)
    header = next(budget_data)
    for row in budget_data:
        date.append(row[0])
        profit_loss.append(row[1])

#cast all elements of profit_loss as integers
profit_loss = [ int(row) for row in profit_loss]

for i in range(len(profit_loss)-1):
    change.append(profit_loss[i+1] - profit_loss[i])

#Summarize data
months = sum(1 for row in date)

net = sum(profit_loss)

avg_change = round(sum(change)/len(change),2)

max_change = max(change)
max_index = change.index(max_change) +1
max_date = date[max_index]

min_change = min(change)
min_index = change.index(min_change) +1
min_date = date[min_index]

#Create, write and read Analysis file
analysis = open('Financial_Analysis.txt','w+')

lines = ['Financial Analysis \n',
    "--------------------------------\n',
    'Total Months: ' + str(months) + '\n',
    'Total: $' + str(net) + '\n',
    'Average Change: $' + str(avg_change) + '\n',
    'Greatest Increase in Profits: ' + max_date + ' ($' + str(max_change) + ') \n',
    'Greatest Decrease in Profits:' + min_date + ' ($' + str(min_change) + ')']

analysis.writelines(lines)
analysis.close()
analysis = open('Financial_Analysis.txt','r+')
print(analysis.read())