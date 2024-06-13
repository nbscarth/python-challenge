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
    pl_changes = []
    prev_column2 = 0
    
    for row in csv_reader:
        total_months += 1

        column2 = int(row[1])
        total_PL += column2 

        # ave_change = sum(row - prev row)/ number
        change = column2 - prev_column2
        pl_changes.append(change)
        prev_column2 = column2

    # Average change calculation
    total_changes = 0
    for value in pl_changes:
        total_changes += value
    ave_change = round(total_changes / total_months, 2)

    # Greatest increase and decrease in profits
    increase = 0
    decrease = 0
    for value in pl_changes:
        if value > increase:
            increase = value
        if value < decrease:
            decrease = value

    # Print statements
    print(total_months)
    print(total_PL)
    print(ave_change)
    print(increase)
    print(decrease)