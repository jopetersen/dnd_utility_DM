import random

i = 4
dice_roll=[]
while i > 0:
	dice_roll.append(random.randint(1,6))
	i -= 1
	
print (dice_roll)

dice_roll.remove(min(dice_roll))
print (dice_roll)

print(sum(dice_roll))