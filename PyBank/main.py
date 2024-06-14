import os
import csv

# Pathing from python-challenge repo
budget_csv = os.path.join("PyBank/Resources/budget_data.csv")

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Gets header and skips for following code
    csv_header = next(csv_reader)
    
    # Variables
    total_months = 0
    total_PL = 0
    pl_changes = []
    prev_column2 = 0
    increase = 0
    decrease = 0 
    dates = []

    for row in csv_reader:
        # Tallies months
        total_months += 1

        # Sums profit/loss
        column2 = int(row[1])
        total_PL += column2 

        # Creating PL change list
        change = column2 - prev_column2
        if row[0] == "Jan-10": # Used start date to establish baseline
            prev_column2 = column2
        else:
            pl_changes.append(change)
            prev_column2 = column2

        # Creating date list
        dates.append(row[0])

    # Average change calculation
    total_changes = 0
    for value in pl_changes:
        total_changes += value
    ave_change = round(total_changes / (total_months - 1), 2)

    # Greatest increase and decrease in profits   
    for value in pl_changes:   
        if value > increase:
            increase = value
        if value < decrease:
            decrease = value

    # Finding date of increase and decrease using list indices
    increase_index = pl_changes.index(increase)
    increase_month = dates[increase_index + 1]
    decrease_index = pl_changes.index(decrease)
    decrease_month = dates[decrease_index + 1]

    # Print statements
    print("Final Analysis")
    print("--------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_PL}")
    print(f"Average Change: ${ave_change}")
    print(f"Greatest Increase in Profits: {increase_month} (${increase})")
    print(f"Greatest Decrease in Profits: {decrease_month} (${decrease})")

# Export results
output_file = os.path.join("PyBank/analysis/final_analysis.txt")

with open(output_file, "w") as textfile:
    writer = csv.writer(textfile, delimiter=",")
    writer.writerow(["Final Analysis"])
    writer.writerow(["--------------------------------------"])
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Total: ${total_PL}"])
    writer.writerow([f"Average Change: ${ave_change}"])
    writer.writerow([f"Greatest Increase in Profits: {increase_month} (${increase})"])
    writer.writerow([f"Greatest Decrease in Profits: {decrease_month} (${decrease})"])