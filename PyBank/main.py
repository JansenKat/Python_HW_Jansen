import csv
with open('Resources/budget_data.csv', newline='') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    months = sum(1 for row in budget_data)-1
    print("Total Months: "+ str(months))