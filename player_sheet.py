from helpers import dice_roll

class Player:
    def __init__(self, name, id, money, properties, houses, hotels, pos, isAlive):
        self.name = name
        self.id = id
        self.money = money
        self.properties = properties
        self.houses = houses
        self.hotels = hotels
        self.pos = pos
        self.isAlive = isAlive
        self.inJail = -1

    def move(self, steps):
        self.pos += steps
        if (self.pos > 39):
            self.pos -= 39
        return self.pos

    def get(self, cash):
        self.money += cash

    def lose(self, cash):
        self.money -= cash

    def buy(self, cost, property):
        if self.money < cost:
            print("Not enough money to buy this property!")
        else:
            self.money -= cost
            self.properties.append(property)

    def pay_rent(self, rent, landlord):
        if landlord.isAlive and landlord.inJail == -1:
            self.money -= rent
            landlord.money += rent
        else:
            print("...but {a} is in jail right now, so, too bad!".format(a=landlord.name))
    
    def go_to_jail(self):
        self.pos = 10
        self.inJail = 0

    def prison_break(self):
        if self.inJail < 0: # Debug test
            print("Something's wrong here. I'm not in jail!")
            quit()
        escape_roll = dice_roll([0,0])
        if escape_roll[1] == 1: # If double is rolled
            self.inJail = -1
            print("{a}'s plea bargain was successful so now {a} is out!".format(a=self.name))
            return escape_roll
        else: # If double is not rolled
            self.inJail += 1
            print("{a}'s plea bargain was unsuccessful. {a} has now spent {b} nights in jail.".format(a=self.name, b=self.inJail))

        if self.inJail == 3:
            self.money -= 50
            self.inJail = -1
            print("{a} has paid $50 to the bank, and is now free!".format(a=self.name))
        return escape_roll