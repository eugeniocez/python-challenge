import os
import csv

#path to the csv file

csvpath=os.path.join('Resources', 'election_data.csv')

#initialize variables

total_votes=0
candidates={}
winner=''

#read the csv file

with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile)

    #skip the header row

    csv_header=next(csvreader)

    #loop through rows in the csv file
    for row in csvreader:

        #update total votes
        total_votes=total_votes+1

        #extract candidate name from the row
        candidate_name=row[2]

        #if candidate is already in the dictionary, increment vote count
        if candidate_name in candidates:
            candidates[candidate_name]=candidates[candidate_name]+1

        else:
            candidates[candidate_name]=1

#calculate the percentage of votes each candidate won and find winner
max_votes=0
with open('Analysis/election_results.txt','w') as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('---------------------------\n')
    txtfile.write(f'Total Votes: {total_votes}\n')
    txtfile.write('---------------------------\n')
    for candidate, votes in candidates.items():
        percentage=(votes/total_votes)*100
        txtfile.write(f'{candidate}:{percentage:.3f} ({votes})\n')
        if votes > max_votes:
            max_votes=votes
            winner=candidate
    txtfile.write('---------------------------\n')
    txtfile.write(f'Winner: {winner}\n')
    txtfile.write('---------------------------\n')

#print analysis to terminal
print('Election Results')
print('---------------------------')
print(f'Total Votes: {total_votes}')
print('---------------------------')

for candidate, votes in candidates.items():
    percentage=(votes/total_votes)*100
    print(f'{candidate}: {percentage:.3f}% ({votes})')
print('---------------------------')
print(f'Winner: {winner}')
print('---------------------------')

print('Results exported to Analysis/election_results.txt')