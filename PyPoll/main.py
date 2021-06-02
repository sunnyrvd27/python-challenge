# import directories
import os
import csv

# declare variables
total_votes = 0
khan_pct = 0
khan_votes = 0
correy_pct = 0
correy_votes = 0
li_pct = 0
li_votes = 0
otooley_pct = 0
otooley_votes = 0
winner_name = " "
winner_votes = 0

# input file 
poll_csv = os.path.join("Resources","election_data.csv")

# output file
output_txt = os.path.join('Analysis','Analysis.txt')

# read input file without header
with open(poll_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
# loop the file to identify the important data 
    for row in csvreader:
# The total number of votes cast
        total_votes = total_votes + 1
# Total Amount complete list of candidates who received votes
# The total number of votes each candidate won
        if row[2] == "Khan":
            khan_votes = khan_votes + 1

        if row[2] == "Correy":
            correy_votes = correy_votes + 1

        if row[2] == "Li":
            li_votes = li_votes + 1

        if row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1
# The percentage of votes each candidate won
    khan_pct = round(((khan_votes/total_votes) * 100), 3)
    correy_pct = round(((correy_votes/total_votes) * 100), 3)
    li_pct = round(((li_votes/total_votes) * 100), 3)
    otooley_pct = round(((otooley_votes/total_votes) * 100), 3)

# The winner of the election based on popular vote 
    if winner_votes < khan_votes:
        winner_votes = khan_votes
        winner_name = "Khan"

    if winner_votes < correy_votes:
        winner_votes = correy_votes
        winner_name = "Correy"

    if winner_votes < li_votes:
        winner_votes = li_votes
        winner_name = "Li"

    if winner_votes < otooley_votes:
        winner_votes = otooley_votes
        winner_name = "O'Tooley"

# print the final analysis
print(f"Election Results")
print(f"------------------------------------------")
print(f"Total Votes: {total_votes}")
print(f"------------------------------------------")
print(f"Khan: {khan_pct}00% ({khan_votes})")
print(f"Correy: {correy_pct}00% ({correy_votes})")
print(f"Li: {li_pct}00% ({li_votes})")
print(f"O'Tooley: {otooley_pct}00% ({otooley_votes})")
print(f"------------------------------------------")
print(f"Winner: {winner_name}")
print(f"------------------------------------------")

# write the analysis in an text file  
with open(output_txt,'w') as txtfile:
#    csvwriter = csv.writer(csvfile, delimiter=',')
    txtfile.writelines("Election Results")
    txtfile.write('\n')
    txtfile.writelines("------------------------------------------")
    txtfile.write('\n')
    txtfile.writelines("Total Votes: " +str(total_votes) )
    txtfile.write('\n')
    txtfile.writelines("------------------------------------------")
    txtfile.write('\n')
    txtfile.writelines("Khan: " +str(khan_pct) +"00% (" + str(khan_votes) + ")")
    txtfile.write('\n')
    txtfile.writelines("Correy: " +str(correy_pct) +"00% (" + str(correy_votes) + ")")
    txtfile.write('\n')
    txtfile.writelines("Li: " +str(li_pct) +"00% (" + str(li_votes) + ")")
    txtfile.write('\n')
    txtfile.writelines("O'Tooley: " +str(otooley_pct) +"00% (" + str(otooley_votes) + ")")
    txtfile.write('\n')
    txtfile.writelines("------------------------------------------")
    txtfile.write('\n')
    txtfile.writelines("Winner: " +str(winner_name) )
    txtfile.write('\n')
    txtfile.writelines("------------------------------------------")
    txtfile.write('\n')
