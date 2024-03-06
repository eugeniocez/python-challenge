import os
import csv

#path to the csv file

csvpath=os.path.join('Resources', 'election_data.csv')

#initialize variables

total_votes=0
candidates=[]
winner=''

#read the csv file

with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile)

    #skip the header row

    csv_header=next(csvreader)

    