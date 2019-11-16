#import csv methods
import csv
#open and read budget_data
with open('Resources/budget_data.csv', newline='') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=' ', quotechar='|')
   
#count months (rows) in budget_data
    months = sum(1 for row in budget_data)-1
    
#print Financial Analysis
    print("Financial Analysis")
    print("--------------------------------")
    print("Total Months: "+ str(months))