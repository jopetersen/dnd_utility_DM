import random

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
new_character(stats)