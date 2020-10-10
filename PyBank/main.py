
import os
import csv

my_folder = os.path.dirname(os.path.abspath('budget_data.csv'))
csvpath = os.path.join(my_folder,"Resources",'budget_data.csv')

# created to store the total number of months
total_months = 0
# created to store the total amount of "Profit/Losses"
total_profits = 0
# created to store the average of the changes
total_average_change = 0
# Dictionary created to store Date as a Key and the the amount change of each month
myBudgetData = {}

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
         
    # Read the header row
    csv_header = next(csvreader)
    for row in csvreader:
        # count total number of months in the dataset 
        total_months += 1
        # sum total amount of "Profit/Losses" 
        total_profits += int(row[1])
       
        # Calculate and save into the dictionay the 'amount change' from the second date
        if total_months > 1 :
           # save the date(row[0]) as key and the difference between current amount and previous amount as value
           myBudgetData[row[0]]= int(row[1]) - v_old_profit
    
        # save the previous amount
        v_old_profit = int(row[1])

# Function that returns the average change (sum values from the dictionay divided by the total months less the first month)
def average_change():
    return(sum(myBudgetData.values())/ (total_months -1)) 

# Function that returns the greatest increase in profits (date and amount) 
def greatest_increase():
    return(str(max(myBudgetData, key=myBudgetData.get)) + ' ($' + str( max(myBudgetData.values()))+')')

# Function that returns the greatest decrease in losses (date and amount)
def greatest_decrease():
    return(str(min(myBudgetData, key=myBudgetData.get)) + ' ($' + str( min(myBudgetData.values()))+')')

# Function that prints to the terminal and exports the result to a text file
def print_ouputs():

    # print to the terminal
    print('-------------------------------------')
    print('Financial Analysis')
    print('-------------------------------------')
    print('Total Months: ',total_months)
    print('Total: $'+str(total_profits))
    total_average_change = average_change()
    print('Average Change: $'+format(total_average_change,',.2f'))
    print('Greatest Increase in Profits: ',greatest_increase())
    print('Greatest Decrease in Profits: ',greatest_decrease())

    # export the text file
    analysis_output = os.path.join("analysis", "financial_analysis.txt")
    with open(analysis_output, 'w') as analysis_txt:
         analysis_txt.write('Election Results:\n')
         analysis_txt.write('-------------------------------------\n')
         analysis_txt.write('Financial Analysis\n')
         analysis_txt.write('-------------------------------------\n')
         analysis_txt.write('Total Months: ' + str(total_months) + '\n')
         analysis_txt.write('Total: $'+str(total_profits) +'\n')
         analysis_txt.write('Average Change: $'+format(total_average_change,',.2f') + '\n')
         analysis_txt.write('Greatest Increase in Profits: ' + greatest_increase() + '\n')
         analysis_txt.write('Greatest Decrease in Profits: '+ greatest_decrease() + '\n')
        
print_ouputs()