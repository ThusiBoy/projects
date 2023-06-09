import random


def dealer_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculator_score(cards):
    """ take a list of cards and returns the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):

    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "you lose opponent got blackjack"
    elif user_score == 0:
        return "you win got a blackjack"
    elif user_score > 21:
        return "you went over 21, you lose"
    elif computer_score > 21:
        return "your opponent went over 21, you win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"


def play_game():
    user_cards = []
    computer_cards = []
    game_over = False
    for _ in range(2):
        user_cards.append(dealer_card())
        computer_cards.append(dealer_card())

    while not game_over:

        user_score = calculator_score(user_cards)
        computer_score = calculator_score(computer_cards)

        print(f" your cards: {user_cards} and your current score: {user_score}")
        print(f" computer first cards: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
        else:
            draw_card = input("Type 'y' to draw another card, Type 'n' to pass ").lower()
            if draw_card == 'y':
                user_cards.append(dealer_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(dealer_card())
        computer_score = calculator_score(computer_cards)

    print(f" Your final hand:{user_cards},Your final score: {user_score}")
    print(f" computer's' final hand:{computer_cards},computer's' final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n' ") == "y":
    play_game()


