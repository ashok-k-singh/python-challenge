# This is the first Python assignment
import os
import csv

# define the files
file_to_load = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("Analysis", "PyBank_Analysis.csv")


# define the function to print the PyBank Analysis 
def print_analysis(mylist, mymonths):
    total_profit = 0 
    change_in_profit = 0
    greatest_inc = 0
    greatest_dec = 0
    cur_change_in_profit = 0
    inc_month = 0
    dec_month = 0
    count = 0  
    
    total_months = len(mylist)
    print(f"Total Months: {total_months}")

    for myprofit in mylist:
        total_profit += int(myprofit)
        if count != 0:
            # do not count first month because the change starts from the second month
            cur_change_in_profit = int(mylist[count]) - int(mylist[count-1]) 
            change_in_profit += cur_change_in_profit 

            # IF neeeded , adjust the greatest profit or losses
            if cur_change_in_profit > greatest_inc:
                greatest_inc = cur_change_in_profit
                inc_month = count
            elif cur_change_in_profit < greatest_dec:
                greatest_dec = cur_change_in_profit
                dec_month = count

        count += 1

    # doing average of total_months-1 because the change starts from the second month 
    average_change_in_profit = int (change_in_profit / (total_months-1))

    # Print the output to the terminal
    print("\n")
    print("******************************************************")
    print("Financial Analysis of PyBank")
    print(f"Total Profit/Losses over the entire period: ${total_profit}")
    print(f"Average Changes in Profit/Losses over the entire period: ${average_change_in_profit}")  
    print(f"Greatest Increase in Profit: {mymonths[inc_month]} ${greatest_inc}")  
    print(f"Greatest Decrease in Profit: {mymonths[dec_month]} ${greatest_dec}")  
    print("******************************************************")    

    # Opne the output file and write the output to the file
    with open(output_file, "w") as my_output_file:
        my_output_file.write("\n ******************************************************")
        my_output_file.write("\n Financial Analysis of PyBank")
        my_output_file.write(f"\n Total Profit/Losses over the entire period: ${total_profit}")
        my_output_file.write(f"\n Average Changes in Profit/Losses over the entire period: ${average_change_in_profit}")  
        my_output_file.write(f"\n Greatest Increase in Profit: {mymonths[inc_month]} ${greatest_inc}")  
        my_output_file.write(f"\n Greatest Decrease in Profit: {mymonths[dec_month]} ${greatest_dec}")  
        my_output_file.write("\n ******************************************************") 
        my_output_file.close()


# Initialize the variables
profit = []
months = []
row_count = 0

#open the data file and read using csv reader
with open(file_to_load, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        months.append(row[0])
        profit.append(row[1])
        row_count += 1

    # Call the Print Analysis Function    
    print_analysis(profit, months)






