import random
import csv

#open the csv file & create a random encounter
with open('csv_files/tiefling_male_names.csv', 'r') as f:
	reader = csv.reader(f)
	your_list = list(reader)
	list_upper_limit = len(your_list)

	random_index = random.randint(0, list_upper_limit)

print(your_list[random_index])