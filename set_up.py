from pandas import *
from pprint import pprint
from player_sheet import *
import time

def generate_board():
    board = []
    xls = ExcelFile('monopoly_properties.xlsx')
    df = xls.parse(xls.sheet_names[0])
    for index,row in df.iterrows():
        temp_dct = {}
        temp_dct['name'] = row['name']
        temp_dct['value'] = row['value']
        temp_dct['type'] = row['type']
        temp_dct['pos'] = row['pos']
        temp_dct['hs_cost'] = row['hs_cost']
        temp_dct['rent'] = row['rent']
        if row['ownable'] == 'yes':
            temp_dct['owned'] = False
            temp_dct['owned_by'] = "Unowned"
        else:
            temp_dct['owned'] = None
            temp_dct['owned_by'] = None
        temp_dct['no_of_houses'] = 0
        temp_dct['visits'] = 0
        board.append(temp_dct)
    return board

def form_players():
    players = []
    num_play, patience = 0, 3
    while (num_play < 2) or (num_play > 8):
        num_play = input("How many players are playing? ")
        
        # Make sure it is a number
        if not num_play.isnumeric():
            print("Type in a number, please!")
            num_play = 0
            patience -= 1
            if patience == 0: # Now look what you've done!
                time.sleep(1)
                print("...")
                time.sleep(2)
                print("ok i'm out")
                time.sleep(1)
                print("bye")
                time.sleep(1)
                quit()
            continue

        # Make sure correct number of players
        num_play = int(num_play)
        if (num_play < 2):
            print("Not enough players. Try again!")
        if (num_play > 8):
            print("Too many players. Try again!")


    for i in range(num_play):
        name = input("Player {i} name: ".format(i=i+1))
        lst = []
        temp_player = Player(name, (i+1), 1500, lst, 0, 0, 0, True)
        players.append(temp_player)
    return players
