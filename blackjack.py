import random

##################################################
# Global Variables

my_cards = []
cp_cards = []

deck = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"A":[1,11],"J":10,"Q":10,"K":10}
deck_cards = list(deck.keys())


##################################################
# # Methods 

def total_count(cards):
    sum = 0
    num_of_aces = 0

    # we add all the cards that are not Aces and store the count of Aces so we can treat them separatly 
    for card in cards:
        if isinstance(deck[card], int):
            sum += deck[card]
        else :
            num_of_aces += 1

    # in case we have Aces in our hand
    if num_of_aces > 0:         
        sum += num_of_aces - 1                   # we add (n-1) Aces as 1, because we can only have maximum one Ace with value 11 without exceding 21
        sum += 11 if sum + 11 <= 21 else 1       # now we treat the remaing Ace

    return sum


def clear_hands():
    my_cards.clear()
    cp_cards.clear()

def play():
    you_want_to_lose_your_home = True
    while you_want_to_lose_your_home == True:
        clear_hands()

        # Draw initial hands for cp
        while total_count(cp_cards) < 17:
            cp_cards.append(random.choice(deck_cards))
        cp_hand_count = total_count(cp_cards)

        # Draw initial hand for myself
        my_cards.append(random.choice(deck_cards))
        my_cards.append(random.choice(deck_cards))
        my_hand_count = total_count(my_cards)

        print(f"\n    Your cards: " + str(my_cards))
        print(f"    Computer's first card: ['{cp_cards[0]}']")

        # Start the game
        hit = my_hand_count < 21
        while hit == True:
            hit = input(" Type 'y' to get another card. type 'n' to pass: ") in ['y','yes']
            if hit == True:
                my_cards.append(random.choice(deck_cards))
                my_hand_count = total_count(my_cards)
                print("     Your cards: " + str(my_cards))
           
            if my_hand_count >= 21 or hit == False:
                break

        print("\n   Your final hand: " + str(my_cards))
        print("     Computer's final hand: " + str(cp_cards))

        print("     Your total count is: " + str(my_hand_count))
        print("     Cp's total count is: " + str(cp_hand_count))
                
       
        if (my_hand_count == 21 
                or (my_hand_count < 21 
                    and cp_hand_count > 21 or (cp_hand_count <= 21 and cp_hand_count < my_hand_count)
                )
            ):
            print("     You win!")
        else:
            print("     You lose!")

        you_want_to_lose_your_home = input("\n Do you want to lose your home? ") in ['y','yes']


##################################################
# Let's start the madness
play()

##################################################