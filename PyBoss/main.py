import csv

with open('Employee_Analysis.csv','w+') as clean:
    fields = ['Emp ID','First Name','Last Name','DOB','SSN','State']
    writer = csv.DictWriter(clean, fieldnames=fields)
    writer.writeheader()
    new_row={}
    
    with open('employee_data.csv','r') as in_data:
        data = csv.DictReader(source)
        full_name = []
        #Read, split name, and write row
        #may be able to ise dict or list comprehension for this
        for row in data:
            new_row = row[:]
            name = new_row.pop(1).split(' ')
            new_row.insert(1,name[0])
            new_row.insert(2,name[1])
            writer.writerow(new_row)
    
