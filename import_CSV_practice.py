import csv

with open('encounters.csv', 'r') as f:
	reader = csv.reader(f)
	your_list = list(reader)
	length_of_list = len(your_list)
print(length_of_list)
