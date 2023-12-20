from pyfiglet import Figlet
import random

def random_dice_generator():
    return random.randint(1, 6)

f = Figlet(font='larry3d')
Intro = ''''''
print(f.renderText('Yahtzee'))
print('initiallizing game.....')
 
num_of_dice = 5
while True:
    dices_rolled = []
    dices_chosen = []
    for i in range(num_of_dice):
        dice = random_dice_generator()
        dices_rolled.append(dice)
    print(dices_rolled)
    picks = input("What dice would you like to pick? (Ask in form of 1 2 3 4 5): ").split()
    picks = "".join(picks)
    print(picks)
    for x in str(picks):
        dices_chosen.append(dices_rolled[int(x) - 1])#could subtract len of num_of_dice 
    num_of_dice = 5 - len(dices_chosen)
    print(dices_chosen)
    if num_of_dice < 1:
        break