# Will's Adventure

"""
As part of an online course, I'm trying to create an Adventure-esque game.
We'll see if this works.
"""


def entrance():
    print "This is the entrance."


def start():
    print "Welcome to Will's Adventure."
    print "Please enter your heroe's name."

    name = raw_input("> ")
    player_name = name.upper()

    print "Welcome %s!" % player_name
    print "Are you ready to begin?"

    _ready = raw_input("> ")
    ready = _ready.lower()

    if ready == "yes" or ready == "y":
        entrance()
    elif ready == "no" or ready == "n":
        print "The sweet smell of adventure is calling!"
    else:
        print 'Please enter either "yes" or "no".'

start()
