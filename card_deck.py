from card import Card
import random
class Deck():
    def __init__(self) -> None:
        self.cards = {}
       
      
           
    def select_card(self):
        card = self.cards.get(random.choice(list(self.cards)))       
        self.cards.pop(card.name)        
        return card
    
    def shuffle_cards(self):
        self.cards = {}
        for number in range(1,14):            
            if number == 1:
                heart = Card("Hearts", 1, "Ace")
                heart.name = "Ace of Hearts"
                club =Card("Clubs", 1, "Ace")
                diamond =Card("Diamonds", 1,"Ace")
                spade =Card("Spades", 1, "Ace")
                self.cards.update({heart.name:heart,club.name:club, spade.name:spade, diamond.name:diamond})
            elif number == 11:
                heart = Card("Hearts", 10, "Jack")
                club =Card("Clubs", 10, "Jack")
                diamond =Card("Diamonds", 10,"Jack")
                spade =Card("Spades", 10, "Jack")
                self.cards.update({heart.name:heart,club.name:club, spade.name:spade, diamond.name:diamond})
            elif number == 12:
                heart = Card("Hearts", 10, "Queen")
                club =Card("Clubs", 10, "Queen")
                diamond =Card("Diamonds", 10,"Queen")
                spade =Card("Spades", 10, "Queen")
                self.cards.update({heart.name:heart,club.name:club, spade.name:spade, diamond.name:diamond})
            elif number == 13:
                heart = Card("Hearts", 10, "King")
                club =Card("Clubs", 10, "King")
                diamond =Card("Diamonds", 10,"King")
                spade =Card("Spades", 10, "King")
                self.cards.update({heart.name:heart,club.name:club, spade.name:spade, diamond.name:diamond})
            else:
                heart = Card("Hearts", number, str(number))
                club =Card("Clubs", number, str(number))
                diamond =Card("Diamonds", number, str(number))
                spade =Card("Spades", number, str(number))
                self.cards.update({heart.name:heart,club.name:club, spade.name:spade, diamond.name:diamond})
        