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
    #print(len(profit_loss))
    #capture changes in profit_loss
    #len -1 to exclude final element
    for i in range(len(profit_loss)-1):
        change.append(profit_loss[i+1] - profit_loss[i])

###Begin Analysis
    #count months (rows) in date array
    months = sum(1 for row in date)
    #sum Profit/Losses Column
    net = sum(profit_loss)
    #average change array, rounded to hundredths place
    #this is not returning the correct value
    avg_change = round(sum(change)/len(change),2)
    #find value/index/date of max value in change array
    #+1 to account for shift when calculating diff between elements
    max_change = max(change)
    max_index = change.index(max_change) +1
    max_date = date[max_index]
    #find value/index/date of min value in change array
    #+1 to account for shift when calculating diff between elements
    min_change = min(change)
    min_index = change.index(min_change) +1
    min_date = date[min_index]

##Text File
#Create text file
analysis = open("Financial_Analysis.txt","a")
#put all strings in a list
lines = ["Financial Analysis \n","-------------------------------- \n",
    "Total Months: "+ str(months)+"\n","Total: $"+str(net)+"\n","Average Change: $"+str(avg_change)+"\n",
    "Greatest Increase in Profits: "+max_date+" ($"+str(max_change)+") \n",
    "Greatest Decrease in Profits:"+min_date+" ($"+str(min_change)+")"]
#write string List to text file
analysis.writelines(lines)
#close file to change access mode
analysis.close()
#open file to read
analysis = open("Financial_Analysis.txt","r+")
#print contents
print(analysis.read())