

def iterative_sum(number):
    if number == 1:
        return number #To ensure not a forever loop
    else:
        return number + iterative_sum(number - 1)


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
    return f"{Reference}\n3 of a kind: {three_of_a_kind} \n4 of a kind: {four_of_a_kind} \nFull House: {Full_House}\nSmall Straight: {Small_Straight}\nLarge Straight: {Large_Straight}\nChance: {chance}\nYahtzee: {Yahtzee}"
l = [1, 2, 3, 4, 6]
l2 = [1, 1, 1, 1, 1]
a = Score_card(l)
print(a)
a = Score_card(l2)
print(a)
#Need to fix how I detect straights
#Need to make it so that 3 of a kind or 4 of a kind only return the totals of all 5 dice and not all 6 sides