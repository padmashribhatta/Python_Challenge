# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:14:59 2024

@author: User
"""

import csv

# Read the financial data from the CSV file
csv_path = 'C:/Users/User/.spyder-py3/GitHub/Python_Challenge/PyBank/Resources/budget_data.csv'

total_months = 0
net_total = 0
changes = []
dates = []

with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_months += 1
        net_total += int(row[1])
        if dates:
            changes.append(int(row[1]) - prev_profit_loss)
        dates.append(row[0])
        prev_profit_loss = int(row[1])

average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Find corresponding dates for greatest increase and decrease
increase_date = dates[changes.index(greatest_increase) + 1]
decrease_date = dates[changes.index(greatest_decrease) + 1]

# Print and export results
output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {increase_date} (${greatest_increase})
Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})
"""

print(output)

with open("financial_analysis.txt", "w") as output_file:
    output_file.write(output)
