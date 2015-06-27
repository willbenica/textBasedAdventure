# Will's Adventure

"""
As part of an online course, I'm trying to create an Adventure-esque game.
We'll see if this works.
"""
from sys import exit

# player = ['name', 'sword', 'arrows', 'num_arrows', 'key1', 'key2']
player = ['', '', '', '', '', '']


def main_hall():
    print "You have entered the main hall of the dragon's lair."


def entrance():
    entrance_desciption = """
    %s, you are standing at the entrance to the Dragon's lair.
    Ahead you will face a plethora of dangers.
    If you feel brave type "ready" to enter, or type "run away" to leave.
    """ % player[0]
    print entrance_desciption
    while True:
        choice = raw_input("> ").lower()
        if choice == "ready":
            main_hall()
        elif choice == "run away":
            dead("You are a coward! Your name has been erased for all time")
        else:
            print "The GODS do not understand."


def restart():
    print "%s, are you ready to begin?" % player[0]
    choice = raw_input("> ").lower()
    if choice == "yes" or choice == "y":
            entrance()
    elif choice == "no" or choice == "n":
        print 'The sweet smell of adventure is calling! \nYou can exit the game by typing "exit".'
        restart()
    elif choice == "exit":
        exit(0)
    else:
        print 'Please enter either "yes" or "no".'


def start():
    print "Welcome to Dragon's Lair Adventure."
    print "Please enter your heroe's name."

    player[0] = raw_input("> ").upper()

    print "Welcome %s!" % player[0]
    print "Are you ready to begin?"

    choice = raw_input("> ").lower()
    while True:
        if choice == "yes" or choice == "y":
            entrance()
        elif choice == "no" or choice == "n":
            print "The sweet smell of adventure is calling!"
            restart()
        elif choice == "exit":
            exit(0)
        else:
            print 'Please enter either "yes" or "no".'


def dead(reason):
    print reason, "\n" * 10
    start()

start()
