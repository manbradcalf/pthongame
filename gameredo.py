from sys import exit

#replacting dis stuff

#now I will begin work on global_dicts

your_stats = {"hp":20,"ammo":20,"hp_scan":20}

def dead(why):
	print why
	exit(0)

def start(a):

	print "---START STARTS HERE---"

	print "You enter a dark, dingy room"
	print "You stub your toe and look downward"
	print "How convenient...a rifle...\n...and %d rounds" % your_stats["ammo"]
	print "You grab the old armor hanging on the wall"
	print "Instructions read: Good for %d HP" % your_stats["hp"]
	print "There are two doors"
	print "Do you choose the Red Door\n...or the Blue door?"

	start_choice = raw_input("> ")

	if "red" in start_choice or "Red" in start_choice:

		monster_HP = 6
		monster_attack = 3

		red_one(your_stats, monster_HP,monster_attack)

	elif "blue" in start_choice or "Blue" in start_choice:

		monster_HP = 2

		blue_one(your_stats, monster_HP,monster_attack)

def red_one(your_stats, monster_HP,monster_attack):

	print "---RED_ONE STARTS HERE---"

	print "You enter with %d HP, %d Ammo and %d HP scans" % (your_stats["hp"],your_stats["ammo"],your_stats["hp_scan"])
	print "You point your rifle at the monster before you"

	your_stats,monster_HP,monster_attack = shoot(your_stats,monster_HP,monster_attack)

	while monster_HP > 0:
		get_shot(your_stats,monster_HP,monster_attack)
		shoot(your_stats,monster_HP,monster_attack)

def blue_one(your_stats, monster_HP,monster_attack):

	print "---BLUE_ONE STARTS HERE---"

	print "You enter with %d HP, %d Ammo and %d HP Scans" % (your_stats["hp"],your_stats["ammo"],your_stats["hp_scan"])
	print "'Got dam smells like shit', you mutter"
	print ""
	print "You point your rifle at the weird, slimy before you"

	your_stats,monster_HP,monster_attack = shoot(your_stats,monster_HP,monster_attack)

	while monster_HP > 0:
		your_stats,monster_HP,monster_attack = get_shot(your_stats,monster_HP,monster_attack)
		your_stats,monster_HP,monster_attack = shoot(your_stats,monster_HP,monster_attack)


def shoot(your_stats, monster_HP,monster_attack):

	print "---shoot STARTS HERE---"

	print "You have %d HP left" % your_stats["hp"]
	print "How many shots do you fire?"

	shots_fired = raw_input("> ")
	shots_fired = int(shots_fired)

	your_stats["ammo"] = your_stats["ammo"] - shots_fired
	monster_HP = monster_HP - shots_fired

	if monster_HP <= 0:
		print "You killed it!"
		print "You now have %d bullets left" % your_stats["ammo"]
		print "You finally look around the room"
		print "There is a door going straight"
		print "There is a door going left"
		room_choose()

	else:
		print "you have %d bullets left" % your_stats["ammo"]
		print "the monster has %d HP left" % monster_HP

	return your_stats, monster_HP,monster_attack

def get_shot(your_stats,monster_HP,monster_attack):

	print "---GET_SHOT STARTS HERE---"

	your_stats["hp"] = your_stats["hp"] - monster_attack

	if your_stats["hp"] <= 0:
		dead('you ran outta HP GOODBYE U DED')

	else:
		print "you take a hit, but survive!"
		print "You have %d HP left" % your_stats["hp"]
		return your_stats, monster_HP,monster_attack

start(your_stats)

#def room_choose(your_stats,monster_HP,monster_attack):