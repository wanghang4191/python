
from sys import exit

def gold_room():

    print("The room is full of gold, how much do u take? ")

    next = input("> ")

    if "0" in next or "1" in next:

        how_much = int(next)

    else:

        dead("Man, learn to input a number. ")

    if how_much < 50:

        print("Nice, you are not greedy. You win! ")

    else:

        dead("You greedy bastard. ")

def bear_room():

    print("There is a bear here. ")

    print("The bear has a bunch of honey. ")

    print("The fat bear is in front of another door. ")

    print("How are you going to move the bear . ")

    bear_moved = False

    while True:

        next = input("> ")

        if next == "take honey":

            dead("The bear look at you , then slap your face off. ")

        elif next == "taunt bear" and not bear_moved:

            print("The bear is move from the door , you can go through it. ")

            bear_moved = True

        elif next == "taunt bear" and bear_moved:

            dead("The bear get pissed off and chews your legs off. ")

        elif next == "open door" and bear_moved:

            gold_room()

        else:

            print("I got no idea what's that mean. ")

def cthulhu_room():

    print("Here you see the great evil cthulhu. ")

    print("It,he,whatever stares at you and you go insane. ")

    print("Do you flee for your life or eat your head. ")

    next = input("> ")

    if "flee" in next:

        start()

    elif "head" in next:

        dead("Well that was tasty!")

    else:

        cthculhu_room()

def dead(why):

    print(why, "Good job!")

    exit(0)

def start():

    print("You are in a dark room")

    print("There is a door to your right and left")

    print("which one do you like")

    next = input("> ")

    if next == "left":

        bear_room()

    elif next == "right":

        cthulhu_room()

    else:

        dead("You stumble around the room until you starve.")

start()


        


         

