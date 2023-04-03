import random
 
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return self.suit + ' of ' + self.value  # This is used to return a string instead of the object reference
 
    def present(self):
        return self.value + ' of ' + self.suit 
 
class Deck:
    def __init__(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [Card(suit, value) for suit in suits for value in values]  # This creates the card object and puts it in a list <-- Most complex line

    def shuffle(self):
        random.shuffle(self.cards)
 
    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop() # Removes the last item in the list (by default if no position is specified) and also returns that value.
 
    def count_remaining(self):
        return len(self.cards)
	
    def get_remaining(self):
        return [x.present() for x in self.cards]    # Calls the present() method on each of the Card objects in the list, returns a list *notice the square brackets*


deck_one = Deck()   # Create the deck
deck_one.shuffle()  # Shuffle the cards

for hand in range(5):   # Deal the cards
    print(deck_one.deal()) # This prints the object reference, not very practical (unless you override the default output with __str__ method)

print(deck_one.count_remaining())   
print(deck_one.get_remaining())