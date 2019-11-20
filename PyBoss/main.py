import csv

with open('Employee_Analysis.csv','w+') as output:
    out_header = ['Emp ID','First Name','Last Name','DOB','SSN','State\n']
    writer = csv.writer(output)
    writer.writerow(out_header)
    new_row = []
    with open('employee_data.csv','r') as in_data:
        data = csv.reader(in_data)
        in_header = next(data)
        for row in data:
            new_row = row[:]
            name = new_row.pop(1).split(' ')
            new_row.insert(1,name[0])
            new_row.insert(2,name[1])
            writer.writerow(new_row)
    
