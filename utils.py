import os
from art import *
from card_deck import Deck

def clear_screen():
   os.system("cls" if os.name == "nt" else "clear") 
   
def header_message():
    clear_screen()
    print(text2art("Black Jack 21"))    

def print_scores(player_1, player_2):
    player_1.print_score()
    player_2.print_score()

def keep_playing(player):
    if player.score > 21:             
        return False
    elif player.score < 21:            
        return True
    
def reset(players):
  print("reseting players")
  for player in players:
    player.cards = []
    player.score = 0           
       
    
    
           