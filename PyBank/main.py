import os
import csv

date = []
profit_loss = []
change = []

#Open & parse budget_data
with open(os.path.join('Resources','budget_data.csv'), 'r') as csvfile:
    budget_data = csv.DictReader(csvfile)
    for row in budget_data:
        date.append(row['Date'])
        profit_loss.append(row['Profit/Losses'])

#cast all elements of profit_loss as integers
profit_loss = [int(row) for row in profit_loss]

for i in range(len(profit_loss)-1):
    change.append(profit_loss[i+1] - profit_loss[i])

#Summarize data
months = len(date)
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
    '--------------------------------\n',
    f'Total Months: {months}\n',
    f'Total: ${net}\n',
    f'Average Change: ${avg_change}\n',
    f'Greatest Increase in Profits: {max_date} (${max_change}) \n',
    f'Greatest Decrease in Profits: {min_date} (${min_change})']

analysis.writelines(lines)
analysis.close()
analysis = open('Financial_Analysis.txt','r')
print(analysis.read())