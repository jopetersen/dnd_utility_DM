import random
import csv
from tkinter import *


race_list = ['human', 'halfling', 'half-orc', 'tiefling', 'dwarf', 'elf', 'dragonborn']
gender = ['male', 'female']

#create a tkinter window
root = Tk()

#open window having dimension 100x100
root.geometry = ('200x200')



#create a dropdown menu that outputs the value of the race to the console 
race_pick = StringVar(root)
race_pick.set(race_list[0]) #default value
w = OptionMenu(root, race_pick, *race_list)
w.pack()


gender_pick = StringVar(root)
gender_pick.set(gender[0]) #default value
w = OptionMenu(root, gender_pick, *gender)
w.pack()


def ok():
	print("value is: " + race_pick.get())


#Create a random encounter generator for D&D

#open the csv file & create a random encounter
def rand_encounter():
	with open('encounters.csv', 'r') as f:
		reader = csv.reader(f)
		your_list = list(reader)
		list_upper_limit = len(your_list)
		random_index = random.randint(0, list_upper_limit)

	print(your_list[random_index])

button = Button(root, text="OK", command = ok)
button.pack()
#create a button
btn = Button(root, text = 'Generate a random encounter !', bd = '5', command = rand_encounter)

#set the position of the button on the top of the window
btn.pack(side = 'top')

#initialize a dictionary of stats
stats = {'strength': 0, 'dexterity': 0, 'intelligence': 0, 'constitution': 0, 'charisma': 0, 'wisdom': 0}

#creates random stats for a new NPC
def new_character(stats):
	for key, val in stats.items():
		#roll a 6 sided die 4 times and remove the lowest value
		i = 4
		dice_roll=[]
		while i > 0:
			dice_roll.append(random.randint(1,6))
			i -= 1
		dice_roll.remove(min(dice_roll))
		stat_value=sum(dice_roll)

		#update the dictionary with the new stat value
		d1 = {key: stat_value}
		stats.update(d1)
	print(stats)



# get a random name based on the race that you choose
def rand_name(race, gender):
	with open('csv_files/tiefling_male_names.csv', 'r') as f:
		reader = csv.reader(f)
		your_list = list(reader)
		list_upper_limit = len(your_list)

		random_index = random.randint(0, list_upper_limit)

	print(your_list[random_index])

root.mainloop()