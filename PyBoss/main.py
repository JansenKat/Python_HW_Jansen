import csv

with open('Employee_Analysis.csv','w+') as output:
    out_header = ['Emp ID','First Name','Last Name','DOB','SSN','State\n']
    writer = csv.writer(output)
    writer.writerow(out_header)
    new_row = []
    with open('employee_data.csv','r') as input:
        data = csv.reader(input)
        in_header = next(data)
        row = next(data)
        new_row = row[:]
        name = new_row.pop(1).split(' ')
        new_row.insert(1,name[0])
        new_row.insert(2,name[1])
        print(new_row)