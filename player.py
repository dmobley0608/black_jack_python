from card import Card
from art import *
class Player():
    def __init__(self, name) -> None:
        self.name = name
        self.cards = []
        self.score = 0
        
    def get_score(self):
        if len(self.cards) > 0:
            values = []
            for card in self.cards:
                values.append(card.value)
            self.score = sum(values)
        
    def hit_me(self, card):
        if type(card) is Card and self.score < 21:
            if card.value == 1 and self.score <= 10:
                card.value = 11            
            self.cards.append(card)            
        self.get_score()
        if(self.score > 21):
                for card in self.cards:
                    if(card.value == 11):
                        card.value = 1
        self.get_score()
        
    def print_score(self): 
        print("-"*55)      
        print(f"{self.name}: cards: {self.cards} score: {self.score}")
        print("-"*55)
      

        
        
        