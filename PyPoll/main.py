#import my dependencies
import os
import csv

#define my file path
election_csv = os.path.join('Resources', 'election_data.csv')

#create starting tallies for all vote categories
totalvotes = 0
candidate_1 = 0
candidate_2 = 0
candidate_3 = 0
candidate_4 = 0

#open csv reader
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

#loop to calulcate vote totals
for candidate in csvreader:
    totalvotes += 1
    if candidate[2] == "Khan":
        candidate_1 += 1
    elif candidate[2] == "Correy":
        candidate_2 += 1
    elif candidate[2] == "Li":
        candidate_3 += 1
    elif candidate[2] == "O'Tooley":
        candidate_4 += 1

cnd1_pct = (candidate_1 / totalvotes) * 100
cnd2_pct = (candidate_2 / totalvotes) * 100       
cnd3_pct = (candidate_3 / totalvotes) * 100
cnd4_pct = (candidate_4 / totalvotes) * 100

all_runners = candidate_1 + candidate_2 + candidate_3 + candidate_4

winner = max(all_runners)

# print statements
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {totalvotes}")
print(f"---------------------------")
print(f"Kahn: {cnd1_pct}({candidate_1})")
print(f"Correy: {cnd2_pct}({candidate_2})")
print(f"Li: {cnd3_pct}({candidate_3})")
print(f"O'Tooley: {cnd4_pct}({candidate_4})")
print(f"---------------------------")
print(f"Winner: {winner}")
print(f"---------------------------")  
