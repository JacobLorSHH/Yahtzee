import random
from pyfiglet import Figlet
#Dice Random Generator
def Dice_Gen(num_of_dice):
	list_of_dice = []
	for i in range(num_of_dice):
		list_of_dice.append(random.randint(1, 6))
	return(list_of_dice)

f = Figlet(font='larry3d')
Intro = ''''''
print(f.renderText('Yahtzee'))
print('initiallizing game.....')


dice_art = {
    1: ["┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"],
    2: ["┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"],
    3: ["┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"],
    4: ["┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"],
    5: ["┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"],
    6: ["┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"]
}

Dices_rolled = Dice_Gen(5) 
print(Dices_rolled)
rolls = 3
while rolls != 0:
    hasnt_passed = True
    while hasnt_passed: 
        hasnt_passed = False 
        picks = input("What dice would you like to keep? (Ask in form of 1 2 3 4 5)>")
        picks = picks.split() 
        picks = "".join(picks) 
        dice_range = ['1', '2', '3', '4', '5']
        dices_chosen = []
        index_of_dices_chosen = []
        for index in picks:
            if (index in dice_range) and (index not in index_of_dices_chosen): #
                dices_chosen.append(Dices_rolled[int(index)-1])
                index_of_dices_chosen.append(index)
            else:
                print("Invalid input! Select a value(1-5) and you cannot pick the same dice more than once")
                hasnt_passed = True
                break
    print(dices_chosen)
    if rolls > 0:
        r_s = input(f"These are the dice you picked. Do you want to reroll the dice in play or score(You have {rolls} rolls left)? (r, s)> ")
        if str(r_s).lower() == 'r':
            rolls -= 1
            remaining_dice = 5 - len(dices_chosen)
            Dices_rolled = dices_chosen 
            Dices_rolled += Dice_Gen(remaining_dice) 
            print(Dices_rolled)
        elif str(r_s) == 's':
            break
    else:
         break
print("This is your final score!")