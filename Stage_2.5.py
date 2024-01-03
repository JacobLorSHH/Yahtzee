import random
from pyfiglet import Figlet


#Dice Random Generator
def Dice_Gen(num_of_dice):
	list_of_dice = []
	for i in range(num_of_dice):
		list_of_dice.append(random.randint(1, 6))
	return(list_of_dice)

def Score_board_display(Ace, Two, Three, Four, Five, Six, three_of_a_kind, four_of_a_kind, short_straight, large_straight, full_house, chance, yahtzee):
    print("Select your score:")
    return f"0. Ace: {Ace}\n1. Two: {Two}\n2. Three: {Three}\n3. Four: {Four}\n4. Five: {Five}\n5. Six: {Six}\n6. Three of a kind: {three_of_a_kind}\n7. Four of a kind: {four_of_a_kind}\n8. Short Straight: {short_straight}\n9. Large Straight: {large_straight}\n10. Full House {full_house}\n11. Chance: {chance}\n12. Yahtzee: {yahtzee}"

def iterative_sum(number):
    if number == 1:
        return number #To ensure not a forever loop
    else:
        return number + iterative_sum(number - 1)
#maybe apply switch statements to make code more legible. 
Bonus = False #Setting Bonus as a global variable
def Score_card(Dices_in_play):
    #Need to make some initiallization thing for all the values. 
    #Ace
    Num_of_Aces = 0
    #Twos
    Num_of_Twos = 0
    #Threes
    Num_of_Threes = 0
    #Fours
    Num_of_Fours = 0
    #Fives
    Num_of_Fives = 0
    #Sixes
    Num_of_sixes = 0
    #Total: Total of all dice in play
    Total = 0
    #Dice instances which the program should check for further pointage
    check = []
    # Finding matches of 3 and two for full house validation
    three_of_a_pair = None
    two_of_a_pair = None
    Full_House = 0
    #Straights
    faces_in_play = []
    straight = 0 #Straight counter, the number of instances where a different dice val appears
    Small_Straight = 0
    Large_Straight = 0
    # Value for all of the dice sides
    Total_of_all_dice_side = iterative_sum(6)
    #Three of a kind and four of a kind
    three_of_a_kind = 0
    four_of_a_kind = 0
    #Yahtzee
    Yahtzee = 0
    Bonus = False
    for dice in Dices_in_play:
        if dice == 1:
            Num_of_Aces += 1
        elif dice == 2:
            Num_of_Twos += 1
        elif dice == 3:
            Num_of_Threes += 1
        elif dice == 4:
            Num_of_Fours += 1
        elif dice == 5:
            Num_of_Fives += 1
        else:
            Num_of_sixes += 1
    Ace = Num_of_Aces * 1
    if Ace > 0:
        Total += Ace
        check.append(Num_of_Aces)
        faces_in_play.append(1)
    Twos = Num_of_Twos * 2
    if Twos > 0:
        Total += Twos
        check.append(Num_of_Twos)
        faces_in_play.append(2)
    Threes = Num_of_Threes * 3
    if Threes > 0:
        Total += Threes
        check.append(Num_of_Threes)
        faces_in_play.append(3)
    Fours = Num_of_Fours * 4
    if Fours > 0:
        Total += Fours
        check.append(Num_of_Fours)
        faces_in_play.append(4)
    Fives = Num_of_Fives * 5
    if Fives > 0:
        Total += Fives
        check.append(Num_of_Fives)
        faces_in_play.append(5)
    Sixes = Num_of_sixes * 6
    if Sixes > 0:
        Total += Sixes
        check.append(Num_of_sixes)
        faces_in_play.append(6)
    #Basic piece of code used to ensure that the values of a small straight are from least to greatest in stepping pattern. 
    S_G = False
    first = 0
    second = 0
    for val in range(len(faces_in_play)):
        if first != 0:
            second = first
        first = min(faces_in_play)
        faces_in_play.remove(first)
        if second != 0:
            if first - second == 1:
                S_G = True
                pass
            else:
                S_G = False
                break
    for duplicates in check:
        #3 and 4 of a kind
        if duplicates > 2:
            if duplicates == 5 and Bonus:
                Yahtzee += 100
            elif duplicates == 5 and not Bonus:
                Yahtzee += 50
                Bonus = True
            if duplicates >= 3:
                three_of_a_kind += Total_of_all_dice_side
            if duplicates >= 4:
                four_of_a_kind += Total_of_all_dice_side
        #Full House
        if duplicates == 3:
            three_of_a_pair = True
        if duplicates == 2:
            two_of_a_pair = True
        if three_of_a_pair and two_of_a_pair:
            Full_House += 25
        if duplicates != 0:
            straight += 1
        if straight == 4 and S_G:
            Small_Straight += 30
        if straight == 5:
            Large_Straight += 40
    chance = Total
    Reference = [Ace, Twos, Threes, Fours, Fives, Sixes] #Seperate these with indentations
    #finding threes
    return Ace, Twos, Threes, Fours, Fives, Sixes, three_of_a_kind, four_of_a_kind, Small_Straight, Large_Straight, Full_House, chance, Yahtzee 

#Need to fix how I detect straights
#Need to make it so that 3 of a kind or 4 of a kind only return the totals of all 5 dice and not all 6 sides


f = Figlet(font='larry3d')
Intro = ''''''
print(f.renderText('Yahtzee'))
print('initiallizing game.....')


dices_in_play = Dice_Gen(5) 
print(dices_in_play)
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
                dices_chosen.append(dices_in_play[int(index)-1])
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
            dices_in_play = dices_chosen 
            dices_in_play += Dice_Gen(remaining_dice) 
            print(dices_in_play) 
        elif str(r_s) == 's':
            break
    else:
         break
print("This is your final score!")
Score_card = Score_card(dices_in_play)
#print(Score_card)
#print(Score_card[0], Score_card[1], Score_card[2], Score_card[3], Score_card[4], Score_card[5], Score_card[6], Score_card[7], Score_card[8], Score_card[9], Score_card[10], Score_card[11])
print(Score_board_display(Score_card[0], Score_card[1], Score_card[2], Score_card[3], Score_card[4], Score_card[5], Score_card[6], Score_card[7], Score_card[8], Score_card[9], Score_card[10], Score_card[11], Score_card[12]))
