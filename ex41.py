
from sys import exit

from random import randint

def death():

	quips = ["You died.You kinda suck at this.",
	"Nice job, you died ... jackass.",
	"Such a luser.",
	"I have a small puppy that's better at this."]

def central_corridor():

	print("The Gothons of Planet Percal # 25 habe invaded your ship and des troyed.")

	print("Your entire crew. You are the last surviving member and your last.")

	print("mission is to get the neutron dseturct bomb from the Weapons Armory")

	print("Put it in the bridge, and bolw the ship up agter getting into an")

	print("escape pod")

	print("\n")

	print("you're running down the central corridor to the weapons armory when")

	print("a gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume")

	print("flowing around his hate filled body . He's blocking the door to the")

	print("Armory and about to pul a weapo to blast you")

	action = input ("> ")

	if action == "shoot!":

		print("Quick on the fraw you yank out your blaster and fire it at the gothon.")

		print("His clown costume is flowing and mobing around his body, whick throws")

		print("off your aim. Your laser hists his coustume but misses him entrely. thsi")

		print("completely ruins his brand new coustume his mother bouhght hism whic")

		print("makes him fly ine an insane rage and blast you repeatdely in the face until")

		print("you are dea s. then he eats you")

		return 'death'

	elif action == "dodge!":

		print("like a world class boxer you dodge , weave,slip and slide right")

		print("as the gothon's blaster cranke a laser past your head.")

		print("in the middel of our artful dodge your foot slips ansd you")

		print("bang your head on the metal wall and psss out")

		print("you wake up shortly agre only to die as the gothon stipls on")

		print("your head and eats you")

		return 'death'

	elif action == "tel a joke":

		print("lucky for you they made your learn gothon insults int he academy")

		print("you tel the one gothon joke you konw")

		print("lvhe abfure vf fb sng , ujra fur fvfg nebhaq gurubhfr, fur fvfgf bebhaq fur ubhfr")

		print("the gotnon stops ,tries not to laugh, then busts out laughing and can't move")

		print("while he's laughing you run up and shott him suqate in the fead")

		print("putting him down , then jump through the weapon armory door")

		return 'laser_weapon_armory'

	else:

		print("does not compute@")

		return 'central_corridor'

def laser_weapon_armory():

	print("you do a dive roll into the weapon armory, crouch and can the room")

	print("for more gothon that might be hiding. It's dead quite, too quite.")

	print("You stand up and run to the far side of the room and find eht")

	print("neutron bomb in its container. There;s a leypad lock on the box ")

	print("and you need the code to get ethbomb out. ig you get the code ")

	print("wrong 10 times then the olck closes forever and hyou can't")

	print("get the bomb. the code is 3 digits.")

	code = "%d%d%d" %(randint(1,9),randit(1,9),randit(1,9))

	guess = input("[keypad]> ")

	guesses = 0

	while guess != code and guesses < 10:

		print("BZZZEDDD")

		guesses += 1

		guess == input("[keypad]> ")

	if guess == code :

		print("the container clicks open and the seal breaks, letting gas out.")

		print("you grab the neutron bomb and run as gast as you can to the")

		print("bridge where you must place it in the right spot")

		return 'the_bridge'

	else:

		print("The lock buzzes one last time and then you hear a sickening")

		print("melting sound asthe mechanism is fused togther")

		print("you decide to sit there, and finally the gotnons bolw up the")

		print("shop fro mthere shop and you die")

		return 'death'

def the_bridge():

	print("you burst onto the bridge with the neuteon destruct")

	print("under your arm and sruprise 5 gothons who sre rtying to")

	print("take control of the ship . each of them has an enen uglier")

	print("clown sostume than the last. they havent pulled their")

	print("weapons out yt, asthy see the active bomb under your")

	print("arm and don't want to st it off")

	action = input("> ")

	if action == "throw the bomb":

		print("in a panic you throe the bomb at the group of gothon ")

		print(" and make a leap for the door. right as your drop if a")

		print("gothon shoots you righti n the back killing you")

		print("as you die you see another gothon frntically ty to disarm")

		print("the bom  your die konwing thy will probably bolw p when")

		print("it goes off")

		return 'death'

	elif action ==  "slowly place the bomb":

		print("you point your blaseter at the bomb under yout arm")

		print("and the gothons put their hands up and start to sweat")

		print("youtinch backewar to the foor, poen it, and then carefully")

		print("place the bomb onthe floor, poing yout blaster at it.")

		print("yout then jump cakc throuth the foor , punch the close button")

		print("and blast the lock so the gothons can't get out")

		print("now that the bomb is palced yout tun to the escape pod tp")

		print("now that the bobm is palced you unr to the escape od to")

		print("get ofo this thin can.")

		return 'escape_pod'

	else :

		print("does nt compte")

		return 'the_bridge'

def escape_pod():

	print("ou rush through the shop desperately trying to make it to")

	print("the escape pod befor the whloe ship explodes . It semms like")

	print("hardly and gothons are on the ship , so yout tun is clear of")

	print("interference you get to the chamber with the escape pld , and")

	print("now needto pick one to take dome of them could be damaged")

	print("buttyout don't have time to look. there;s 5pods whick one")

	print("do you take")

	good_pod = randint(1,5)

	guess = input("[pod #]> ")

	if int(guess) != good_pod:

		print("youtjump into pod %s and hit the eject butto." %guess)

		print("the pod escapes out into the boid of space, then")

		print("implodes as the hull ruptures , vrushing your body")

		print("into jam jekky")

		return 'death'

	else:

		print("you jump into pod %s hit the eject button"%guess)

		print("the pod easily slides out into space hearing to")

		print("the plante belos. as ti files to the plantr you look")

		print("back and see your ship impolde then explode like a ")

		print("bright star, taking out the gothon ship at the same")

		print("time. yout wom")

		exit(0)

ROOMS = {
'death': death,
'central_corridor': central_corridor,
'laser_weapon_armory': laser_weapon_armory,
'the_bridge': the_bridge,

'escape_pod':escape_pod

}

def runner(map, start):

	next = start

	while True:

		room = map[next]

		print("\n--------")

		next = room()

runner(ROOMS, 'central_corridor')

