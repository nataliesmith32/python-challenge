#import my dependencies
import os
import csv

#define my file path
budget_csv = os.path.join('Resources', 'budget_data.csv')

#open csv reader
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)
    
#create a place to store the data
    totalmonths = []
    yearlyprofit = []
    changeinprofit = []
                         
#loop through csv to find total months and total yearly profit
    for row in csvreader:
        totalmonths.append(row[0])
        yearlyprofit.append(int(row[1]))

#calulcate for average yearly profit
    for i in range(len(yearlyprofit)-1):
        changeinprofit.append(yearlyprofit[i+1]-yearlyprofit[i])
                      
#solve for increase and decrease for the year
greatest_increase = max(changeinprofit)
greatest_decrease = min(changeinprofit)

month_increase = changeinprofit.index(max(changeinprofit))+1
month_decrease = changeinprofit.index(min(changeinprofit))+1

#assign variables for the new data 
all_months = len(totalmonths)
all_profits = sum(yearlyprofit)
avg_change = round(sum(changeinprofit)/len(changeinprofit),2)

# print collected data
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{all_months}")
print(f"Total: ${all_profits}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {totalmonths[month_increase]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {totalmonths[month_decrease]} (${(str(greatest_decrease))})")      

#output to new file
output = os.path.join(".", 'pybank_output.txt')
with open(output,"w") as completed_file:
    completed_file.write("Financial Analysis")
    completed_file.write("\n")
    completed_file.write("------------------------")
    completed_file.write("\n")
    completed_file.write(f"Total Months:{len(totalmonths)}")
    completed_file.write("\n")
    completed_file.write(f"Total: ${sum(yearlyprofit)}")
    completed_file.write("\n")
    completed_file.write(f"Average Change: {round(sum(changeinprofit)/len(changeinprofit),2)}")
    completed_file.write("\n")
    completed_file.write(f"Greatest Increase in Profits: {totalmonths[month_increase]} (${(str(greatest_increase))})")
    completed_file.write("\n")
    completed_file.write(f"Greatest Decrease in Profits: {totalmonths[month_decrease]} (${(str(greatest_decrease))})")
