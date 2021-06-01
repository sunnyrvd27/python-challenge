# import directories
import os
import csv

# declare variables
total_months = 0
total_amt = 0
first_amt = 0
first_amt_flag = "Y"
last_amt = 0
avg_amt = 0
avg_month = 0
curr_value = 0
prev_value = 0
g_increase = 0
g_decrease = 0
date_increase = " "
date_decrease = " "


# input file 
budget_csv = os.path.join("Resources","budget_data.csv")

# output file
output_txt = os.path.join('Analysis','Analysis.txt')

# read input file without header
with open(budget_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
# loop the file to identify the important data 
    for row in csvreader:
        total_months = total_months + 1
        total_amt = total_amt + int(row[1])
        last_amt = int(row[1])

        if first_amt_flag == "Y":
            first_amt = int(row[1])
            first_amt_flag = "N"
            pre_value = 0
        
        curr_value = int(row[1])
        absolute_value = (prev_value - curr_value) * (-1)
        if g_increase < absolute_value:
            g_increase = absolute_value
            date_increase = row[0]

        if g_decrease > absolute_value:
            g_decrease = absolute_value
            date_decrease = row[0]   

        prev_value = int(row[1])   
        
    #    print(f"{date_increase} - {g_increase} and {date_decrease} - {g_decrease}")

    avg_month = total_months - 1
    avg_amt = round(((int(last_amt) - int(first_amt)) / int(avg_month) ),2)

#    print(f"First Amount: {first_amt} & Last Amount: {last_amt} & Average: {avg_amt}")
# Total no.of months
# Total Amount
# 1st Month Profit/Loss Value
# Last month Profit/Loss Value
# Change Average months = Total months - 1
# Greatest increase
# Greatest decrease
 

# print the final values
print(f"Financial Analysis")
print(f"------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amt}")
print(f"Average Change: ${avg_amt}")
print(f"Greatest Increase in profits: {date_increase} (${g_increase})")
print(f"Greatest Decrease in profits: {date_decrease} (${g_decrease})")

# write the analysis in an text file  
with open(output_txt,'w') as txtfile:
#    csvwriter = csv.writer(csvfile, delimiter=',')
    txtfile.writelines("Financial Analysis")
    txtfile.write('\n')
    txtfile.writelines("------------------------------------------")
    txtfile.write('\n')
    txtfile.writelines("Total Months: " +str(total_months) )
    txtfile.write('\n')
    txtfile.writelines("Total: $" +str(total_amt))
    txtfile.write('\n')
    txtfile.writelines("Average Change: $" +str(avg_amt))
    txtfile.write('\n')
    txtfile.writelines("Greatest Increase in profits: " +str(date_increase) +" (S" +str(g_increase) +")" )
    txtfile.write('\n')
    txtfile.writelines("Greatest Decrease in profits: " +str(date_decrease) +" (S" +str(g_decrease) +")")
    txtfile.write('\n')
#    csvwriter.writerow(['Duave','Picardi','111-76-0091'])
#    print("CSV File written")