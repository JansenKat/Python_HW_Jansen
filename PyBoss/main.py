import csv

with open('employee_data.csv','r') as csv:
    data = csv.reader(csv)
    header = next(data)
    