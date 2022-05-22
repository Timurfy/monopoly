from player_sheet import *
from set_up import generate_board, form_players
from helpers import dice_roll, players_alive, property_report
from random import *
import time

def game_start():
    # Set up measurements
    rounds = 0
    free_parking = 0

    # Create players, returns list of players in random order
    playlist = form_players()
    shuffle(playlist)

    # Generate board, a list accessible by position
    board = generate_board()
    print("==========================================")
    print("The game is starting now. Get ready, greedy capitalists!")
    print("==========================================")

    # While players still alive, take turn
    #while players_alive: set this up later
    for x in range(20):
        for player in playlist:
            # Announce round
            if player == playlist[0]:
                rounds += 1
                time.sleep(2)
                print("==========================================")
                print("Round {a} is starting now!".format(a=rounds))
                input("Ready? If so, press ENTER.")
                print("==========================================")

            name = player.name

            if player.inJail >= 0: # If in prison, try to get out
                roll_count = player.prison_break()
            else: # If not in prison, roll dice
                roll_count = dice_roll([0,0])
            old_rep = 0
            new_rep = roll_count[1]
            # If dice roll the same, repeat unless three times
            while (new_rep > old_rep) and (new_rep < 3):
                old_rep = new_rep
                roll_count = dice_roll(roll_count)
                new_rep = roll_count[1]
                if new_rep == 3:
                    print(("{a} rolled the same number thrice, and is going to jail!").format(a=name))
                    player.go_to_jail()
            # If player is in jail, go to next player
            if player.inJail >= 0:
                continue
            
            steps = roll_count[0]
            current_pos = board[player.move(steps)]
            print(("{a} is at {b} now.").format(a=name, b=current_pos['name']))

            # If property is unowned, buy it
            if current_pos['owned'] == False:
                player.buy(current_pos['value'], current_pos['name'])
                current_pos['owned'] = True
                current_pos['owned_by'] = name
                print(("{a} has bought {b} for the price of ${c}.").format(a=name, b=current_pos['name'], c=current_pos['value']))
            
            # Else, if property is owned, pay rent
            elif current_pos['owned'] == True:
                # Find the landlord
                for person in playlist:
                    if person.name == current_pos['owned_by']:
                        landlord = person
                        break
                if landlord == player:
                    print("...which {a} owns, anyway.".format(a=name))
                    continue
                rent = current_pos['rent']
                print(("{a} has paid ${b} to {c} for landing on {d}.").format(a=name, b=rent, c=landlord.name, d=current_pos['name']))
                player.pay_rent(rent, landlord)

            # Else, if property is unownable, do relevant action
            elif current_pos['owned'] == None:
                if current_pos['type'] == 'tax':
                    tax = current_pos['rent']
                    player.lose(tax)
                    free_parking += tax
                    print(("{a} has paid ${b} in taxes to the bank.").format(a=name, b=tax))
                elif current_pos['type'] == 'go_to_jail':
                    player.go_to_jail()
                    print("{a} has landed on Go to Jail, and has been, well, sent to jail.".format(a=name))
                elif current_pos['type'] == 'jail' and player.inJail < 0:
                    print("...but {a} is only visiting.".format(a=name))
                elif current_pos['type'] == 'free_parking':
                    print("Wahoo! {a} has hit landed on Free Parking, and has received ${b}.".format(a=name, b=free_parking))
                    player.get(free_parking)
                    free_parking = 0
        
    for player in playlist:
        b = ''
        for property in player.properties:
            b += property + ', '
        print(("{a} currently owns {b}and has ${c}.").format(a=player.name, b=b, c=player.money))

        # TODO: Add in a winner check at the end of each turn, then break if win
    property_report(board)

game_start()
