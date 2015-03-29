from sys import exit



# need to figure out what to do once ammo and health is below zero



def dead(why):
	print why
	exit(0)


def start():

	Your_HP = 20
	Your_Ammo = 20
	HP_Scan = 2
	your_stats = [Your_HP, Your_Ammo, HP_Scan]

	print "You enter a dark, dingy room"
	print "You stub your toe and look downward"
	print "How convenient...a rifle...\n...and %d rounds" % Your_Ammo
	print "You grab the old armor hanging on the wall"
	print "Instructions read: Good for %d HP" % Your_HP
	print "There are two doors"
	print "Do you choose the Red Door\n...or the Blue door?"

	start_choice = raw_input("> ")

	if "red" in start_choice or "Red" in start_choice:

		initial_monster_HP = 6

		red_one(your_stats, initial_monster_HP)
		
	else:
		print "What the fuck dude"

	if "blue" in start_choice or "Blue" in start_choice:

		initial_monster_HP = 2

		blue_one(your_stats, initial_monster_HP)

	else:
		print "Dowut"



def red_one(your_stats, initial_monster_HP):

	print "----red_one STARTS HERE-----"

	monster_attack = 3

	print "You enter with %d HP, %d Ammo and %d HP_Scans" % (Your_HP, Your_Ammo, HP_Scan)
	print ""

	print "You point your rifle at the monster before you"
	
	shoot_first(initial_monster_HP, your_stats)


	while monster_HP > 0:
		get_shot(monster_attack, monster_HP, your_stats)
		shoot_again(monster_HP)


		


def shoot_first(initial_monster_HP, your_stats):

	print "----shoot_first STARTS HERE-----"


	print "You have %d HP left" % Your_HP
	print "How many shots do you fire?"
	
	shots_fired = raw_input('> ')
	shots_fired = int(shots_fired)

	Your_Ammo = Your_Ammo - shots_fired
	
	initial_monster_HP = initial_monster_HP - shots_fired
	monster_HP = initial_monster_HP

	if monster_HP <= 0:
		print "You killed it!"
		print "You now have %d bullets left" % Your_Ammo
		print "You finally look around the room"
		print "There is a door going straight"
		print "There is a door going left"
		room_choose()

	else:
		print "The monster stumbles but does not die"
		print "You steady your rifle and take aim"


	print "You have %d bullets left" % Your_Ammo
	print "The monster has %d HP left" % monster_HP

	your_stats = [Your_HP,Your_Ammo,HP_Scan]

	return monster_HP, your_stats



def shoot_again(monster_HP, your_stats):

	print "----shoot_again STARTS HERE-----"

	print "You have %d HP left" % Your_HP
	print "How many shots do you fire?"

	shots_fired = raw_input('> ')
	shots_fired = int(shots_fired)

	Your_Ammo = Your_Ammo - shots_fired
	monster_HP = monster_HP - shots_fired

	print "You have %d bullets left" % Your_Ammo
	print "The monster has %d HP left" % monster_HP

	if monster_HP <= 0:
		print "You killed it!"
		print "You now have %d bullets left" % Your_Ammo
		print "You finally look around the room"
		print "There is a door going straight"
		print "There is a door going left"
		room_choose()

	else:
		print "The monster stumbles but does not die"
		print "You steady your rifle and take aim"

	your_stats = [Your_HP, Your_Ammo, HP_Scan]

	return your_stats, monster_HP 




def get_shot(monster_attack, monster_HP,your_stats):

	print "----get_shot STARTS HERE-----"


	monster_HP = monster_HP


	Your_HP = Your_HP - monster_attack

	if Your_HP <= 0:
		dead('You ran out of HP GOODBYE U DED')

	else:
		print "You take a hit, but survive!"
		print "You have %d HP left" % Your_HP
		return monster_attack, Your_HP, monster_HP

def room_choose(your_stats):

	print "Which room do you choose?"
	room_choice = raw_input('> ')

	print "Ok cool you said '%s' but I can't finish this game now sorry" % room_choice
	dead('because its saturday night and im tired and hungry')



start()
	




#def red_two(Your_HP, Your_Ammo, HP_Scan):


def blue_one(your_stats, initial_monster_HP):
	print "blue_one stars here!"
	
	if your_stats = initial
	

#def blue_two():

#def ammo_room():

#def HP_room():

#def boss_room():

#def purple_room():