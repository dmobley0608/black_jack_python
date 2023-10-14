import time
from art import *
from player import Player
from card import Card
from card_deck import Deck
from utils import *

global is_running
is_running = True
# Initialize Players
pc = Player("The Computer")
player = Player("Player 1")


# Initialize Deck of Cards
deck = Deck()
deck.shuffle_cards()


# New Game
def new_game():
    deck.shuffle_cards()
    reset([player, pc])
    play_again = input("Press 'y' to play again.")
    if play_again == "y":
        clear_screen()
        print("Starting new game")
        time.sleep(2)
    else:
        global is_running
        is_running = False


# Welcome
header_message()


# Get players name
# player.name = input("Please enter your name: ")

# Loop for game
while is_running:
    header_message()
    print(len(deck.cards))
    # Check For New Game
    if player.score < 1 and pc.score < 1:
        player.hit_me(deck.select_card())
        player.hit_me(deck.select_card())
        pc.hit_me(deck.select_card())
        pc.hit_me(deck.select_card())
        print_scores(player, pc)
        if player.score > 21 or pc.score == 21:
            tprint("You Lose!")
            new_game()
        if pc.score > 21 or player.score == 21:
            tprint("You Win")
            new_game()
    # If not new Game Print Scores and Take Player Response
    else:
        print_scores(player, pc)

        hit_me = input("'H'it Me  or 'S'tay: ")
        # Hit Me or Stay
        if hit_me.lower() == "h":
            clear_screen()
            header_message()
            # Draw Card
            player.hit_me(deck.select_card())
            # Check Players Score
            if player.score > 21 or pc.score == 21:
                print_scores(player, pc)
                tprint("You Lose!")
                new_game()
            # PC Draw card and Check Pcs Score
            if pc.score < 14 and pc.score > 0 or pc.score < player.score:
                pc.hit_me(deck.select_card())
            if pc.score > 21 or player.score == 21:
                print_scores(player, pc)
                tprint("You Win")
                new_game()

        # Player Chose to stay
        elif hit_me.lower() == "s":
            clear_screen()
            header_message()
            print_scores(player, pc)
            # Check Pc Score and Draw Card if needed
            if pc.score < 14 or pc.score <= player.score:
                pc.hit_me(deck.select_card())
                # If Pc is over 21 start new game
                if pc.score > 21:
                    clear_screen()
                    header_message()
                    print_scores(player, pc)
                    tprint("You Win")
                    new_game()
            # Check to see if pc has 21
            if pc.score == 21:
                tprint("You Lose!")
                new_game()
