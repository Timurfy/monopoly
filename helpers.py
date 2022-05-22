import random
import time

def dice_roll(roll_count):
    roll_1 = random.randint(1,3)
    roll_2 = random.randint(1,3)
    roll_count[0] += (roll_1 + roll_2)
    if roll_1 == roll_2:
        roll_count[1] += 1
    return roll_count

def players_alive(playlist, num_players):
    dead = 0
    for player in playlist:
        if player.isAlive == False:
            dead += 1
        if (dead == (num_players - 1)):
            return False
    return True

def player_report(playlist):
    print("=====================")
    print("PLAYER REPORT")
    print("=====================")
    for player in playlist:
        b = ''
        for property in player.properties:
            b += property + ', '
        print(("{a} currently owns {b}and has ${c}.").format(a=player.name, b=b, c=player.money))

def property_report(board):
    print("=====================")
    print("PROPERTY REPORT")
    print("=====================")
    print("Property ---- Owned by")
    colour = ''
    for property in board:
        if property['owned_by']:
            if property['type'] != colour:
                colour = property['type']
                print()
                print("{a}".format(a=colour.upper()))
            name = property['name']
            owner = property['owned_by']
            print("{a} ---- {b}".format(a=name, b=owner))
    print("=====================")
    print("END OF REPORT")
    print("=====================")

def end_game():
    print("==========================================")
    print("Thank you for playing! Goodbye.")
    print("==========================================")
    time.sleep(1)
