import os
import csv
csvpath = os.path.join ('resources', 'budget_data.csv')

 # Define the function to count the total number of months in the dataset
def count_months(budgetdata):
    # Initialize row count for total number of months
    months_counter = 0
   
    # Read each row of data after the header
    for _ in budgetdata:
        #Increase counter by 1
        months_counter += 1

    # Return the total number of months
    return months_counter

# Define function to calculate the total profits and losses over the entire period
def Sum_ProfitsLosses (budgetdata):
    total_ProfitsLosses = 0

    for row in budgetdata:
        # Add values for total profits and losses from second column (columnindex 1)in csv file
        total_ProfitsLosses += int(row[1])

    return total_ProfitsLosses
# Define function to calculate changes in profits and losses and average of those changes
def calculate_changes_and_average(budgetdata):
    changes = []
    previous_profit_loss = 0

    for row in budgetdata:
        current_profit_loss = int(row[1])
        if previous_profit_loss != 0:
            change = current_profit_loss - previous_profit_loss
            changes.append(change)
        previous_profit_loss = current_profit_loss

    # Calculate average change
    average_change = sum(changes) / len(changes) if len(changes) > 0 else 0

    return changes, average_change
#To find the greatest increase in profits and losses

def find_greatest_increase(changes, budgetdata):
    greatest_increase = max(changes)
    greatest_increase_index = changes.index(greatest_increase)
    greatest_increase_date = budgetdata[greatest_increase_index + 1][0]  # Adding 1 to account for skipping header row

    return greatest_increase, greatest_increase_date

#To find the greatest decrase in profits and losses

def find_greatest_decrease(changes, budgetdata):
    greatest_decrease = min (changes)
    greatest_decrease_index = changes.index(greatest_decrease)
    greatest_decrease_date = budgetdata[greatest_decrease_index + 1][0]  # Adding 1 to account for skipping header row

    return greatest_decrease, greatest_decrease_date

# Open the CSV file and use the function
with open(csvpath) as csvfile:
    budgetdata = list(csv.reader(csvfile, delimiter=','))
    header = budgetdata[0]
    data = budgetdata[1:]

    print ("Financial Analysis\n")

    print ("----------------------------\n")
    
    #Call the function and print the result
    
    total_months = count_months(data)
    print(f"Total Months: {total_months}\n")

    total_ProfitsLosses = Sum_ProfitsLosses(data)
    print(f"Total: ${total_ProfitsLosses}\n")

    changes, average_change = calculate_changes_and_average(data)
    print(f"Average Change: ${round (average_change,2)}\n")

    greatest_increase, greatest_increase_date = find_greatest_increase(changes, data)
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")

    greatest_decrease, greatest_decrease_date = find_greatest_decrease(changes, data)
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
# Open a text file for writing
    output_file_path = os.path.join("analysis", "PybankResults.txt")
    with open(output_file_path, "w") as PyBankResults_file:
        # Write the results to the file
        PyBankResults_file.write("Financial Analysis\n")
        PyBankResults_file.write("------------------\n")
        PyBankResults_file.write(f"Total Months: {total_months}\n")
        PyBankResults_file.write(f"Total: ${total_ProfitsLosses}\n")
        PyBankResults_file.write(f"Average Change: ${round(average_change, 2)}\n")
        PyBankResults_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
        PyBankResults_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

    print(f"Results exported to '{output_file_path}'")