#import csv methods
import csv

#define column variables as arrays
date = []
profit_loss = []
change = []

###Pull Data from CSV into workable forms
#open and read budget_data
with open('Resources/budget_data.csv', newline='') as csvfile:
    budget_data = csv.reader(csvfile)
#add data from csv to arrays
    for row in budget_data:
        date.append(row[0])
        profit_loss.append(row[1])
#remove headers from arrays
    date.pop(0)
    profit_loss.pop(0)
#cast all elements of profit_loss as integers
    profit_loss = [ int(row) for row in profit_loss]
#capture changes in profit_loss
#len -2 to exclude final element
    for i in range(len(profit_loss)-2):
        change.append(profit_loss[i+1] - profit_loss[i])

###Begin Analysis
#count months (rows) in date array
    months = sum(1 for row in date)
#sum Profit/Losses Column
    net = sum(profit_loss)
#average change array, rounded to hundredths place
#this is not returning the correct value
    avg_change = round(sum(change)/len(change),2)
#Find value/index/date of max value in change array
#+1 to account for shift when calculating diff between elements
    max_change = max(change)
    max_index = change.index(max_change) +1
    max_row = date[max_index] + " ($"+str(max_change)+")"

#Find value/index/date of min value in change array
#+1 to account for shift when calculating diff between elements
    min_change = min(change)
    min_index = change.index(min_change) +1
    min_row = date[min_index] + " ($"+str(min_change)+")"


#print statement for testing
print(min_row)


# ##print Financial Analysis
#     print("Financial Analysis")
#     print("--------------------------------")
#     print("Total Months: "+ str(months))
#     print("Total: $"+str(net))
#     print("Average Change: ")
#     print("Greatest Increase in Profits: ")
#     print("Greatest Decrease in Profits:")