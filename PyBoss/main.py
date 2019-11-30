import csv
import datetime as dt

us_state_abbrev = {
    'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE',
    'Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA',
    'Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT','Nebraska': 'NE',
    'Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH',
    'Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX',
    'Utah': 'UT','Vermont': 'VT','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY',
    }

with open('clean_employee_data.csv','w+') as clean:
    fields = ['Emp ID','First Name','Last Name','DOB','SSN','State']
    writer = csv.DictWriter(clean, fieldnames=fields)
    writer.writeheader()
    new_row={}
    
    with open('employee_data.csv','r') as source:
        data = csv.DictReader(source)
        for row in data:
            new_row = row.copy()

            #Separate first and last name
            full_name = new_row.pop('Name')
            full_name = full_name.split(' ')
            new_row['First Name'] = full_name[0]
            new_row['Last Name'] = full_name[1]

            #Convert date format with datetime
            new_row['DOB'] = dt.datetime.strptime(new_row['DOB'], '%Y-%m-%d').strftime('%m/%d/%y')

            #Hide first 5 digits of SSN
            new_row['SSN'] = '***-**-' + new_row['SSN'][-4:]

            #Convert state to ISO code
            new_row['State'] = us_state_abbrev[new_row['State']]
            writer.writerow(new_row)
    
