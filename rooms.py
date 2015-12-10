# turn the rooms into classes and to contain common elements.


class Room(object):
    """
    This is the main class for all rooms. There should be common elements contained within this class. These should make it easier to add new rooms.
    """

    def __init__(self, name, rn, enemyType, numEnemies=0, numDoors=1):
        self.name = name
        self.rn = rn
        self.enenmyType = enenmyType
        self.numEnemies = numEnemies
        self.numDoors = numDoors

        def description(desc):
            print desc

        def choose(choice):
            if choice == 'stats'or choice == 's':
                stats(rn)
            elif choice == 'life' or choice == 'l':
                life(rn)
            elif choice == 'instructions' or choice == 'i':
                instructos(rn)
            elif choice == 'attack':
                attack(plyaer, enemy, rn)
            elif choice == 'search':
                search(item, rn)
            else:
            print "Be more decisive, these are not nice monsters."
            attack(mh_enemy, player, rn)


main_hall = rooms.Room('Main Hall', 2, 'zombie', 1, 2)



###### This has been converted yet.
def main_hall():
    rn = 2
    mh_enemy = enemyRooms[2]
    print "You have entered the main hall of the dragon's lair."
    if mh_enemy.life > 0:
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
            attack(player, mh_enemy, rn)
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
            attack(mh_enemy, player, rn)


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
