class Card():
    def __init__(self,  suite,value, name):
        if value == 11 : name = "Jack"
        if value == 12 : name = "Queen"
        if value == 13 : name = "King"
        if value == 1 : name = "Ace"
        self.value = value
        self.suite = suite
        self.name = f"{name} of {suite}"
        
    def __repr__(self) -> str:
        return self.name
        