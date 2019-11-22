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
            new_row = row.copy()
            full_name = new_row.pop('Name')
            full_name = full_name.split(' ')
            new_row['First Name'] = full_name[0]
            new_row['Last Name'] = full_name[1]
            new_row['DOB'] = datetime.datetime.strptime(new_row['DOB'], '%Y-%m-%d').strftime('%m/%d/%y')
            writer.writerow(new_row)
    
