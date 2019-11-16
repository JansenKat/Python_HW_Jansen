#import csv methods
import csv

#define column variables as arrays
date = []
profit_loss = []

#open and read budget_data
#my csv has headers, do I need to get rid of these?
with open('Resources/budget_data.csv', newline='') as csvfile:
    budget_data = csv.reader(csvfile)
#add data from csv to arrays
#I need to remove the headers, they're in these arrays and they shouldn't be
    for row in budget_data:
        date.append(row[0])
        profit_loss.append(row[1])
    date.pop(0)
    profit_loss.pop(0)
    profit_loss = [ int(val) for val in profit_loss]

#count months (rows) in date array
    months = sum(1 for row in date)-1
#sum Profit/Losses Column
    net = sum(profit_loss)
#average Profit/Losses Column
#this is not returning the correct value
    avg_change = net/len(profit_loss)

#print statement for testing
print(avg_change)


# #print Financial Analysis
#     print("Financial Analysis")
#     print("--------------------------------")
#     print("Total Months: "+ str(months))
#     print("Total: $"+str(net))
#     print("Average Change: ")
#     print("Greatest Increase in Profits: ")
#     print("Greatest Decrease in Profits:")