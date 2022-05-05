import random

class Deck:
    def __init__(self):
        self.card = 0 #card number
        self.score = 300 #total player score
    
    def draw_card(self):
        self.card = random.randint(1,13)
        print(self.card)

        # higher means when the second card > first card = h
    # lower means when the second card < first card = l
        

    def award_points(self):
        self
        

    def keep_score(self):
        if self.score == 0:
            print('game over')

