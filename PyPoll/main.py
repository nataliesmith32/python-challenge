#improt my dependencies
import os
import csv

#define my file path
election_csv = os.path.join('Resources', 'election_data.csv')

#open csv reader
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)

#create a place to store the data
    totalvotes = 0
    candidates = []
    all_votes = []
    data_percentage = []
    most_votes = candidate_votes[0]
    index = 0

  

    
    