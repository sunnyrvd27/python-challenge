# import directories
import os
import csv

# declare variables


# input file 
poll_csv = os.path.join("Resources","election_data.csv")

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



# The total number of votes cast
# Total AmountA complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

 

# print the final values
print(f"Election Results")
print(f"------------------------------------------")
print(f"Total Votes: {total_months}")
print(f"------------------------------------------")
print(f"Khan: ${total_amt}")
print(f"Correy: ${avg_amt}")
print(f"Li: {date_increase} (${g_increase})")
print(f"O'Tooley: {date_decrease} (${g_decrease})")
print(f"------------------------------------------")
print(f"Winner: {date_decrease} (${g_decrease})")
print(f"------------------------------------------")

# write the analysis in an text file  
with open(output_txt,'w') as txtfile:
#    csvwriter = csv.writer(csvfile, delimiter=',')
    txtfile.writelines("Election Results")
    txtfile.write('\n')
    txtfile.writelines("------------------------------------------")
    txtfile.write('\n')
    txtfile.writelines("Total Votes: " +str(total_months) )
    txtfile.write('\n')
    txtfile.writelines("------------------------------------------")
    txtfile.write('\n')
    txtfile.writelines("Khan: " +str(total_amt))
    txtfile.write('\n')
    txtfile.writelines("Correy: " +str(avg_amt))
    txtfile.write('\n')
    txtfile.writelines("Li: " +str(date_increase) +" (S" +str(g_increase) +")" )
    txtfile.write('\n')
    txtfile.writelines("O'Tooley: " +str(date_decrease) +" (S" +str(g_decrease) +")")
    txtfile.write('\n')
    txtfile.writelines("------------------------------------------")
    txtfile.write('\n')
    txtfile.writelines("Winner: " +str(total_months) )
    txtfile.write('\n')
    txtfile.writelines("------------------------------------------")
    txtfile.write('\n')
