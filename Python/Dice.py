import random


class Dice(object):

    def __init__(self, name, color, sides): # this is the constructor for the Dice objects #1
        self.name = name
        self.color = color
        self.sides = sides
        roll = 0
        print(f"You made a dice named: {self.name} and its color is: {self.color}")

    def roll(self):
        self.roll = random.randint(1,self.sides)
        print(f"Your dice:{self.name} color:{self.color} rolled {self.roll}")
        return self.roll

    # making DiceRoll Function    


# ------------- Class Ends HERE ---------------------

# Create 2 different Dice Object using the class
goodDice = Dice("ludo", "red", 6)
badDice = Dice("BadDice","blue",13)


print(goodDice.name)
print(goodDice.roll())

print(badDice.name)
print(badDice.roll())
