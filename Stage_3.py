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
def Score_card(Dices_in_play, chance_condition, yahtzee_condition):
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
    #Chance
    chance = 0
    #Yahtzee
    Yahtzee = 0
    Bonus = yahtzee_condition
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
        if 1 not in faces_in_play:
            faces_in_play.append(1)
    Twos = Num_of_Twos * 2
    if Twos > 0:
        Total += Twos
        check.append(Num_of_Twos)
        if 2 not in faces_in_play:
            faces_in_play.append(2)
    Threes = Num_of_Threes * 3
    if Threes > 0:
        Total += Threes
        check.append(Num_of_Threes)
        if 3 not in faces_in_play: 
            faces_in_play.append(3)
    Fours = Num_of_Fours * 4
    if Fours > 0:
        Total += Fours
        check.append(Num_of_Fours)
        if 4 not in faces_in_play: 
            faces_in_play.append(4)
    Fives = Num_of_Fives * 5
    if Fives > 0:
        Total += Fives
        check.append(Num_of_Fives)
        if 5 not in faces_in_play: 
            faces_in_play.append(5)
    Sixes = Num_of_sixes * 6
    if Sixes > 0:
        Total += Sixes
        check.append(Num_of_sixes)
        if 6 not in faces_in_play:
            faces_in_play.append(6)
    #Basic piece of code used to ensure that the values of a small straight are from least to greatest in stepping pattern. 
    S_G = 0
    first = 0
    second = 0
    for val in range(len(faces_in_play)):
        if first != 0:
            second = first
        first = min(faces_in_play)
        faces_in_play.remove(first)
        if second != 0:
            if first - second == 1:
                S_G += 1
                pass
            else:
                break
    for duplicates in check:
        #3 and 4 of a kind
        if duplicates > 2:
            if duplicates == 5 and Bonus:
                Yahtzee += 100
            elif duplicates == 5 and not Bonus:
                Yahtzee += 50
            if duplicates >= 3:
                three_of_a_kind += Total
            if duplicates >= 4:
                four_of_a_kind += Total
        #Full House
        if duplicates == 3:
            three_of_a_pair = True
        if duplicates == 2:
            two_of_a_pair = True
        if three_of_a_pair and two_of_a_pair:
            Full_House += 25
        if duplicates != 0:
            straight += 1
        if straight == 4 and (S_G > 2):
            Small_Straight += 30
        if straight == 5 and (S_G > 3):
            Large_Straight += 40
    if chance_condition == False:
        chance = Total
    Reference = [Ace, Twos, Threes, Fours, Fives, Sixes] #Seperate these with indentations
    #finding threes
    return [Ace, Twos, Threes, Fours, Fives, Sixes, three_of_a_kind, four_of_a_kind, Small_Straight, Large_Straight, Full_House, chance, Yahtzee] 

#Need to fix how I detect straights
#Need to make it so that 3 of a kind or 4 of a kind only return the totals of all 5 dice and not all 6 sides


f = Figlet(font='larry3d')
print(f.renderText('Yahtzee'))
print('initiallizing game.....')
Chance_and_Yahtzee = []
players_scores = []
num_of_players = int(input("How many players? "))
for i in range(num_of_players):
    username = str(input("Enter players username: "))
    players_scores.append([0,0,0,0,0,0,0,0,0,0,0,0,0,username])
    Chance_and_Yahtzee.append([False, False]) # Chance, Yahtzee
#Set up arrays to store user values
print(players_scores)
for i in range(13):
    print('\n')
    print('\n')
    print('\n')
    f = Figlet(font='larry3d')
    print(f.renderText(f"Game {i + 1}"))
    for current_player in range(len(players_scores)):
        print(players_scores[current_player][-1])
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
        #Allows user to select a score from the listed posibilities above. 
        print("This is your final score!")
        Scores = Score_card(dices_in_play, Chance_and_Yahtzee[current_player][0], Chance_and_Yahtzee[current_player][-1])
        #print(Score_card)
        #print(Score_board_display(Score_card[0], Score_card[1], Score_card[2], Score_card[3], Score_card[4], Score_card[5], Score_card[6], Score_card[7], Score_card[8], Score_card[9], Score_card[10], Score_card[11], Score_card[12]))
        print(Score_board_display(Scores[0] + players_scores[current_player][0], Scores[1] + players_scores[current_player][1], Scores[2] + players_scores[current_player][2], Scores[3] + players_scores[current_player][3], Scores[4] + players_scores[current_player][4], Scores[5] + players_scores[current_player][5], Scores[6] + players_scores[current_player][6], Scores[7] + players_scores[current_player][7], Scores[8] + players_scores[current_player][8], Scores[9] + players_scores[current_player][9], Scores[10] + players_scores[current_player][10], Scores[11] + players_scores[current_player][11], Scores[12] + players_scores[current_player][12]))
        while True: 
            chosen_score = int(input("Select a score: "))
            if chosen_score in range(0, 13):#Range is 0 .... max(n)-1
                players_scores[current_player][chosen_score] += Scores[chosen_score]
                if chosen_score == 11:
                    Chance_and_Yahtzee[current_player][0] = True
                if Scores[chosen_score] == 50:
                    Chance_and_Yahtzee[current_player][-1] = True
                print(Chance_and_Yahtzee)
                print('\n')
                print('\n')
                print('\n')
                print('\n')
                print('\n')
                print('\n')
                print('\n')
                print('\n')
                print('\n')
                print('\n')
                print('\n')
                print('\n')
                print('\n')
                print('\n')
                print('\n')
                print('\n')
                print('\n')
                print(f"This is {players_scores[current_player][-1]}'s current score:")
                print(Score_board_display(players_scores[current_player][0], players_scores[current_player][1], players_scores[current_player][2], players_scores[current_player][3], players_scores[current_player][4], players_scores[current_player][5], players_scores[current_player][6], players_scores[current_player][7], players_scores[current_player][8], players_scores[current_player][9], players_scores[current_player][10], players_scores[current_player][11], players_scores[current_player][12]))
                print('\n')
                print('\n')
                print('\n')
                break
            else:
                print("Invalid! Try again!")
    for current_player in range(len(players_scores)):
        print(f"{players_scores[current_player][-1]}'s current score:")
        print(Score_board_display(players_scores[current_player][0], players_scores[current_player][1], players_scores[current_player][2], players_scores[current_player][3], players_scores[current_player][4], players_scores[current_player][5], players_scores[current_player][6], players_scores[current_player][7], players_scores[current_player][8], players_scores[current_player][9], players_scores[current_player][10], players_scores[current_player][11], players_scores[current_player][12]))