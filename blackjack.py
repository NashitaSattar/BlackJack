#Blackjack/21 game
from blackjack_art import logo
import random
import os

def clear(): #Function to clear the terminal
    os.system('cls')

def deal_card(): #Returns random card from deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(list): #Calculates the sum of the cards 
    if sum(list) == 21 and len(list) == 2: #If we have 21 with only 2 cards
        return 0 #Return score of Blackjack
   
    if 11 in list and sum(list) > 21: #If we are over 21 and have an ace (11)
        list.remove(11)
        list.append(1)
    
    return sum(list) #Return the list after any changes made

def compare(user_score, computer_score): #Compare the player and computer's scores to see who wins
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "You Lose! Computer has a Blackjack."
    elif user_score == 0:
        return "You Win! You had a Blackjack!"
    elif user_score > 21:
        return "You Lose! You went over 21!"
    elif computer_score > 21:
        return "You Win! Computer went over 21!"
    elif user_score > computer_score:
        return "You Win! You had the higher score!"
    else:
        return "You Lose! Computer had the higher score!"

def blackjack():
   
    print(logo)

    user_cards = [] #List to store user's cards
    computer_cards = [] #List to store computer's cards
    is_game_over = False #Boolean to check if the game is over or not

    for dealing in range(2): #Deals two inital cards to user and computer
        user_cards.append(deal_card()) #Add new card to user list
        computer_cards.append(deal_card()) #Add new card to computer list

    while not is_game_over: #This part repeats for the player after initial setup
        user_score = calculate_score(user_cards) #Calculate the user's score
        computer_score = calculate_score(computer_cards) #Calculate the computer's score
        print(f"    Your card: {user_cards}, current score: {user_score} ")
        print(f"    Computer's first hand: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21: #Check if the game is already over by someone getting 21 or user going over 21
            is_game_over = True #Game is now over
        else: #Give user the choice to get another card
            go_again = input("Would you like to draw another card? Type 'yes' or 'no': ") #Give user the choice to get another card     
            if go_again == "yes": #If user want another card give them one and recalculate their score
                user_cards.append(deal_card())     
            else: #If user doesn't want another card the game is over
                is_game_over = True

    while computer_score != 0 and computer_score < 17: #The player is done. The computer will keep drawing cards as long as it doesn't have a blackjack already and the sum is less than 17
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, your final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, computer's final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Would you like to play a game of Blackjack? Type 'yes' or 'no': ") == "yes":
    clear()
    blackjack()