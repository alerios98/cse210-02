from hilo_game import Deck

# import hilo_game.py info
# start hilo game by calling deck class

player1 = Deck()


keep_playing = 'y'
#loops the game until user decides to stop it

while keep_playing == 'y':
# draw 2 cards that will be compared
    first_card = player1.draw_card()
    print(f'The card is: {first_card}')

    second_card = player1.draw_card()

    """
    print(second_card) 
    i'm keeping this here for debugging purposes. Having this print statement 
    allows you to see if the comparison is being done correctly or not
    """
    #have user guess if second card is higher or lower
    guess = input('Higher or lower? [h/l] ').lower()

    #compare guess to actual cards
    #if guess is correct then award points
    #if guess is incorrect then deduct points

    if guess == 'h' and (second_card > first_card):
        player1.award_points()
    elif guess == 'h' and (second_card < first_card):
        player1.deduct_points()
    elif guess == 'l' and (second_card < first_card):
        player1.award_points()
    elif guess == 'l' and (second_card > first_card):
        player1.deduct_points()
    elif guess == 'h' and (second_card == first_card):
        player1.deduct_points()
    elif guess == 'l' and (second_card == first_card):
        player1.deduct_points()


    print(f'Next card was: {second_card}')

    player1.keep_score()
    #award or deduct points based on guess

    #finds score so that it can be compared
    score = player1.game_over_score()
    
    #if player reaches score of 0 or less then the game is over
    if score <= 0:
        keep_playing = 'n'
    #if score is greater than 0 they can continue to play
    else:
        keep_playing = input('Play again? [y/n]: ').lower()
    print()







