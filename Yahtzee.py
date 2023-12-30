from pyfiglet import Figlet
import random

def random_dice_generator():
    return random.randint(1, 6)

f = Figlet(font='larry3d')
Intro = ''''''
print(f.renderText('Yahtzee'))
print('initiallizing game.....')
 









 #User Interface: This is used to get the chosen dice values from the user stored in an array. This information is then processessed in the scoring function which returns a 
num_of_dice = 5
while True:
    dices_rolled = []
    for i in range(num_of_dice):
        dice = random_dice_generator()
        dices_rolled.append(dice)
    print(dices_rolled)
    hasnt_passed = True
    while hasnt_passed:
        hasnt_passed = False
        dices_chosen = []
        dices_chosen_index = []
        picks = input("What dice would you like to pick? (Ask in form of 1 2 3 4 5): ").split()
        picks = "".join(picks)
        for x in str(picks):
            try: 
                if (int(x) > 0 and int(x) <= len(dices_rolled)):#could subtract len of num_of_dice 
                    if  dices_rolled[int(x) - 1] not in dices_chosen:
                        dices_chosen.append(dices_rolled[int(x) - 1])
                    else:
                        print('You cannot choose the same dice twice. The program has thus removed it.')
                else:
                    print('Input must correspond to one of the availible dices')
                    print("Try picking again!")
                    hasnt_passed = True
                    break
            except:
                print("Invalid Input!")
                print("Try picking again!")
                hasnt_passed = True
                break
    num_of_dice -= len(dices_chosen)
    print(num_of_dice)
    print(dices_chosen)
    if num_of_dice < 1:
        break