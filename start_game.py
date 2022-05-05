from hilo_game import Deck

# import hilo game info
# start hilo game by calling deck class? 
player1 = Deck()
first_card = player1.draw_card()
second_card = player1.draw_card()

 # higher means when the second card > first card = h
    # lower means when the second card < first card = l

#card comparison 
if second_card > first_card:
    value = 'h'
elif second_card < first_card:
    value = 'l'






