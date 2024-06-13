import os
import csv

csv_path = r"D:\Scarthicus\Documents\Bootcamp\Challenges\Module_3\python-challenge\PyBank"
budget_csv = os.path.join(csv_path,"Resources","budget_data.csv")

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

# Gets header and skips for following code
    csv_header = next(csv_reader)
    
    total_months = 0
    total_PL = 0
    
    for row in csv_reader:
        total_months += 1

        total_PL += int(row[1]) 

        # ave_change = sum(row - prev row)/ number

    # Print statements
    print(total_months)
    print(total_PL)
