#Make a two-player Rock-Paper-Scissors game.


while True:
    player1 = input('Hello Player1 select Rock, Paper or Scissor: ')
    player2 = input('Hello Player2 select Rock, Paper or Scissor: ')

    if player1.lower() == 'rock' and player2.lower() == 'scissor':
        print('Congrats Player1 you won!')
    elif player1.lower() == 'scissor' and player2.lower() == 'paper':
        print('Congrats Player1 you won!')
    elif player1.lower() == 'paper' and player2.lower() == 'rock':
        print('Congrats Player1 you won!')
    else:
        print('Congrats Player2 you won!')
    choice = input('Do you want to play again?(Yes/No): ')
    if choice.lower() == 'no':
        break
print('Hope you enjoyed the game!')




