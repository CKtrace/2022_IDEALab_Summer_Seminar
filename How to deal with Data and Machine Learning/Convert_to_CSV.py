from concurrent.futures import process
import csv

with open('Sample_Data.txt') as f:
    tab_reader = csv.reader(f, delimiter='\t')
    for row in tab_reader:
        date = row[0]
        evaluation = row[1]
        score = float(row[2])
        process(date, evaluation, score)
        
        