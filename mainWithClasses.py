# dragon_sLairWithClasses

from sys import exit
import random
import math

import character
import weapons

# Create a player which can be modified
player = character.Player("")

# {
#     'name': '',
#     'life':  100,
#     'sword': 'Dull Sword',
#     'swordDamage': 5,
#     'arrows': False,
#     'numArrows': 0,
#     'lavaBoots': False,
#     'airBoots': False,
#     'key1': False,
#     'key2': False
# }

# dict of all possible swords
swordDamages = {
    'Dull Sword': 5,
    'Illuminati Sword': 23,
    'Improbable Sword': 42,
    'Hyrulian Sword': 100,
}

# Enemies
zombie1 = character.Zombie('Zed the Zombie')

# {
#     'name': 'Zed the Zombie',
#     'life': 10,
#     'weapon': 'Gnashing Teeth',
#     'weaponDamage': 1
# }

# dwarf1 = {
#     'name': 'Leon the Large',
#     'life': 25,
#     'weapon': 'Dwarfish Sword',
#     'weaponDamage': 15
# }

# dwarf2 = {
#     'name': 'Dug the Dwarf',
#     'life': 25,
#     'weapon': 'Dwarfish Sword',
#     'weaponDamage': 15
# }

# dwarf3 = {
#     'name': 'Will the Dwarf Lad',
#     'life': 25,
#     'weapon': 'Dwarfish Sword',
#     'weaponDamage': 15
# }

# Which rooms have enemies
enemyRooms = {
    2: zombie1,
    # 3: zombie2
}

rocks1 = {
    'name': 'Zed\'s Fridge',
    'descriptionItemFalse': 'What looked like rocks from afar is really a pile of skulls and brains.',
    'item': False,
    'itemType': None,
    'whichItem': None
}
rocks2 = {
    'name': 'Plain rocks',
    'descriptionItemTrue': 'A plain pile of rocks, with something metallic sticking out.',
    'descriptionItemFalse': 'A plain pile of rocks.',
    'item': True,
    'itemType': 'sword',
    'whichItem': weapons.weapons['Illuminati Sword']
}


def attack(enemy, rn):
    while enemy.life >= 0:
        enemy.life -= player.inventory['weapon']['damage']
        if enemy.life >= 0:
            print "The battle rages on! %s has %d life left.\n" % (enemy.name, enemy.life)
        else:
            print "You have vanquished %s!" % enemy.name
    get_back(rn)


def attackEnemy(enemy, rn):
    while player.life >= 0:
        if math.floor(random.random() * 100) % 7:
            print "%s is attacking." % enemy.name
            player.life -= enemy.inventory['weapon']['damage']
            if player.life >= 0:
                print "The battle rages on! %s has %d life left.\n" % (player.name, player.life)
            else:
                print "%s has vanquished %s!" % (enemy.name, player.name)
        else:
            print "%s has attacked, you have perried masterfully. You return the attack." % enemy.name
            attack(enemy, rn)
    get_back(rn)


def search(item, rn):
    if item['item']:
        print item['descriptionItemTrue'], "\n"
        while item['item']:
            if item['itemType'] == 'sword':
                player.inventory['weapon'] = item['whichItem']
                item['item'] = False
                print "You have found a/n: %s.\n\t %s" % (item['whichItem']['name'], item['whichItem']['description'])
            else:
                print "Nothing to see here, move along.\n"
    else:
        print item['descriptionItemFalse'], "\n"
    get_back(rn)


def get_back(rn):
    if rn == -1:
        restart()
    elif rn == 0:
        restart
    elif rn == 1:
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
    print player.life
    get_back(rn)


def instructos(rn):
    print """
    This is where the instrucions go.
    """
    get_back(rn)


def stats(rn):
    print """
    Name: \t\t%s
    Life: \t\t%s
    Weapon: \t\t%s
    Weapon Description: %s
    Weapon Damage: \t%s
    """ % (player.name, player.life, player.inventory['weapon']['name'], player.inventory['weapon']['description'], player.inventory['weapon']['damage'])
    get_back(rn)


def main_hall():
    rn = 2
    mh_enemy = enemyRooms[2]
    print "You have entered the main hall of the dragon's lair."
    if mh_enemy.life >= 0:
        print "You see 2 rock piles strewn about, and running directly towards you is a zombie.\n"
        print '%s: "BRAAAAIIIIIINSsss, BRAAAAIIIIIINSsss!"' % mh_enemy.name
        print "\n"
        print "What do you do? Attack the zombie or search through the rocks?"
    else:
        print "You see 2 rock piles strewn about."
        print "\n"
        print "Would you like to search through the rocks?"

    while True:
        choice = raw_input("> ").lower()
        if choice == "stats":
            stats(rn)
        elif choice == "life":
            life(rn)
        elif choice == "instructions":
            instructos(rn)
        elif choice == "attack" or choice == "attack zombie":
            attack(mh_enemy, rn)
        elif choice == "search" or choice == "search rocks":
            whichItem = raw_input('Which pile of rocks would you like to search, the "big" or "small" pile?\n> ')
            if whichItem == "big".lower():
                search(rocks1, rn)
            else:
                search(rocks2, rn)
        elif choice == "more":
            get_back()
        else:
            print "Be more decisive, these are not nice monsters."
            attackEnemy(mh_enemy, rn)


def entrance():
    rn = 1
    entrance_desciption = """
    %s, you are standing at the entrance to the Dragon's lair.
    Ahead you will face a plethora of dangers.
    If you feel brave type "ready" to enter, or type "run away" to leave.
    """ % player.name
    print entrance_desciption
    while True:
        choice = raw_input("> ").lower()
        if choice == "stats":
            stats(rn)
        elif choice == "life":
            life(rn)
        elif choice == "i" or choice == "instructions":
            instructos(rn)
        elif choice == "ready":
            main_hall()
        elif choice == "run away":
            dead("You are a coward! Your name has been erased for all time")
        else:
            print "The GODS do not understand."


def restart():
    rn = 0
    print "%s, are you ready to begin?" % player.name
    choice = raw_input("> ").lower()
    if choice == "yes" or choice == "y":
            entrance()
    elif choice == "no" or choice == "n":
        print 'The sweet smell of adventure is calling! \nYou can exit the game by typing "exit".\n'
        restart()
    elif choice == "exit":
        exit(0)
    elif choice == "stats":
            stats(rn)
    elif choice == "life":
            life(rn)
    elif choice == "i" or choice == "instructions":
        instructos(rn)
    else:
        print 'Please enter either "yes" or "no".'
        restart()


def start():
    rn = -1
    print "Welcome to Dragon's Lair Adventure."
    print "Please enter your hero's name."

    player.name = raw_input("> ").upper()

    print "Welcome %s!" % player.name
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
        if choice == "stats":
            stats(rn)
        elif choice == "life":
            life(rn)
        elif choice == "i" or choice == "instructions":
            instructos(rn)
        else:
            print 'Please enter either "yes" or "no".'
            restart()


def dead(reason):
    print reason, "\n" * 10
    start()

start()
