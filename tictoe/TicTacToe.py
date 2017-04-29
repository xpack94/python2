from TicTacToeUtil import *

PLAYER_HUMAN = 'H'
GAME_CONTINUE = 0
done = GAME_CONTINUE
move = -1
clear = "\n" * 100

player_type = {'X': '', 'O': ''}
player_turn = ' '
game_board = range(9)
game_board_legend = range(9)

#Generate game board and legend
for i in game_board:
  game_board[i] = ' '
  game_board_legend[i] = str(i)

#Setup the game and retrieve game settings
while player_type['X'] != 'H' and player_type['X'] != 'A':
  player_type['X'] = raw_input("Is player X human or AI?\nEnter \'H\' for human, \'A\' for AI: ")
  player_type['X'] = player_type['X'].upper()

while player_type['O'] != 'H' and player_type['O'] != 'A':
  player_type['O'] = raw_input("Is player O human or AI?\nEnter \'H\' for human, \'A\' for AI: ")
  player_type['O'] = player_type['O'].upper()

while player_turn != 'X' and player_turn != 'O':
  player_turn = raw_input("Who should go first?\nEnter \'X\' for player X, \'O\' for player O: ")
  player_turn = player_turn.upper()

#Clear the screen
print clear

while done == GAME_CONTINUE:

  #Human gets a turn
  if(player_type[player_turn] == PLAYER_HUMAN):

    print "Your turn (Player " + player_turn + ")"
    print_board(game_board)
    print "\n Legend:\n"
    print_board(game_board_legend)

    move = get_user_move(game_board)

    game_board[move] = player_turn
    done = GameState.check_win(game_board)

    if done != GAME_CONTINUE:
      break

  #Computer plays a turn
  else:
    print "Waiting for " + player_turn + "\'s turn"
    game_tree = generate_game_tree(game_board, player_turn)
    move = generate_best_move(game_tree, player_turn)
    game_board[int(move)] = player_turn
    done = GameState.check_win(game_board)

    if done != GAME_CONTINUE:
      break

  #Switch to the next player
  player_turn = 'X' if player_turn == 'O' else 'O'
  print clear

#Print final results
print_board(game_board)

if done == 'X':
  print "The winner is player X!"
elif done == 'O':
  print "The winner is player O!"
else:
  print "It's a tie!"