# Will's Adventure

"""
As part of an online course, I'm trying to create an Adventure-esque game.
We'll see if this works...
"""
from sys import exit


# Set up a hero who can then be modified
player = {
    'name': '',
    'life':  100,
    'sword': 'Dull Sword',
    'swordDamage': 5,
    'arrows': False,
    'numArrows': 0,
    'lavaBoots': False,
    'airBoots': False,
    'key1': False,
    'key2': False
}

# dict of all possible swords
swordDamages = {
    'Dull Sword': 5,
    'Illuminati Sword': 23,
    'Improbable Sword': 42,
    'Hyrulian Sword': 100,
}

# Enemies
zombie1 = {
    'name': 'Zed the Zombie',
    'life': 10,
    'weapon': 'Gnashing Teeth',
    'weaponDamage': 1

}

# Which rooms have enemies
enemyRooms = {
    2: zombie1,
    3: zombie2
}

rocks1 = {
    'name': 'Zed\'s Fridge',
    'description': 'What looked like rocks from afar is really a pile of skulls and brains.',
    'item': False,
    'itemType': None,
    'whichItem': None
}
rocks_2 = {
    'name': 'Plain rocks',
    'decription': 'A plain pile of rocks, with something metallic sticking out.',
    'item': True,
    'itemType': 'sword'
    'whichItem': 'Illuminati Sword'
}


def attack(enemy, rn):
    while enemy['life'] >= 0:
        enemy['life'] -= player['swordDamage']
        if enemy['life'] >= 0:
            print "The battle rages on! %s has %d life left." % (enemy['name'], enemy['life'])
        else:
            print "You have vanquished %s!" % enemy['name']
    get_back(rn)


def search(item, rn):
    while item['item']:
        if item[itemType] == 'sword':
            player['sword'] = item['whichItem']
            player['swordDamage'] = swordDamages[player['sword']]
            item['item'] = False
            print "You have found a/n: %s." % item['whichItem']
        else:
            print "Nothing to see here, move along."
    get_back(rn)


def get_back(rn):
    if rn == 1:
        entrance()
    elif rn == 2:
        main_hall()
    # elif rn == 3:
    #     west_wing()
    # elif rn == 4:
    #     no_floor()
    # elif rn == 5:
    #     boss_room_west()
    # elif rn == 6:
    #     secretTunnel()
    # elif rn == 7:
    #     east_wing()
    # elif rn == 8:
    #     lava_floor()
    # elif rn == 9:
    #     boss_room_east()
    # elif rn == 10:
    #     lair_entrance()
    # elif rn == 11:
    #     dragon_lair()
    else:
        print "%s, the dragon has awoken. You hear him roar and run back to the entrance.", "\n" * 3, "Isn't this the reason you came here?", "\n" * 3
        entrance()


def life(rn):
    print player[1]
    get_back(rn)


def stats(rn):
    print """
    Name: \t\t%s
    Life: \t\t%s
    Sword: \t\t%s
    Sword Damage: \t%s
    """ % (player[0], player[1], player[2], player[3])
    get_back(rn)


def main_hall():
    rn = 2
    mh_enemy = enemies[0]
    print "You have entered the main hall of the dragon's lair."
    if mh_enemy[2] >= 0:
        print "You see 2 rock piles strewn about, and running directly towards you is a zombie."
        print 'ZOMBIE: "BRAAAAIIIIIINSsss, BRAAAAIIIIIINSsss!"'
        print "\n" * 2
        print "What do you do? Attack the zombie or search through the rocks?"
    else:
        print "You see 2 rock piles strewn about."
        print "\n" * 2
        print "Would you like to search through the rocks?"

    while True:
        choice = raw_input("> ").lower()
        if choice == "stats":
            stats(rn)
        elif choice == "life":
            life(rn)
        elif choice == "attack":
            attack(mh_enemy, rn)
        elif choice == "search":
            search(rocks_2, rn)
        elif choice == "more":
            get_back()
        else:
            print "I'm not done yet."
            entrance()


def entrance():
    rn = 1
    entrance_desciption = """
    %s, you are standing at the entrance to the Dragon's lair.
    Ahead you will face a plethora of dangers.
    If you feel brave type "ready" to enter, or type "run away" to leave.
    """ % player[0]
    print entrance_desciption
    while True:
        choice = raw_input("> ").lower()
        if choice == "stats":
            stats(rn)
        elif choice == "life":
            life(rn)
        elif choice == "ready":
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
