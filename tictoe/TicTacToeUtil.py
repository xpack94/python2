class GameState:
  def __init__(self, game_board, move, player):
    self.game_board = list(game_board)
    self.move = move
    self.children = []
    self.game_end = False

  def generate_children(self, player):
    moves = [i for i, x in enumerate(self.game_board) if x == ' ']

    for move in moves:
      child = GameState(self.game_board, move, player)
      child.game_board[move] = player
      child.set_winner()

      if child.game_end == False:
        child.generate_children('X' if player == 'O' else 'O')
        self.children.append(child)
      else:
        self.children.append(child)


  def set_winner(self):
    #X is given a positive score, O is given a negative score
    winner = GameState.check_win(self.game_board)
    if winner == 'X':
      self.score = 1
      self.game_end = True
    elif winner == 'O':
      self.score = -1
      self.game_end = True
    elif winner == -1:
      self.score = 0
      self.game_end = True
    else:
      self.score = 0
      self.game_end = False

  @staticmethod
  def check_win(game_board):
    winning_moves = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for moves in winning_moves:
      if game_board[moves[0]] == game_board[moves[1]] and game_board[moves[1]] == game_board[moves[2]] and game_board[moves[0]] != ' ':
        return game_board[moves[0]]

    if ' ' not in game_board:
      return -1

    return 0

def get_user_move(game_board):
  while True:
    move = raw_input("Enter 0-8: ")

    if not move.isdigit():
      print "Input is not a number. Please enter an integer between 0-8"
      continue
    else:
      move = int(move)

    if not 0 <= move <= 8:
      print "Input not between 0-8. Please enter an integer between 0-8"
    elif game_board[move] != ' ':
      print "Move is already taken. Pick another move"
    else:
      break

  return move

def print_board(b):
  print '|' + b[0] + '|' + b[1] + '|' + b[2] + '|\n'
  print '|' + b[3] + '|' + b[4] + '|' + b[5] + '|\n'
  print '|' + b[6] + '|' + b[7] + '|' + b[8] + '|\n'

def generate_game_tree(game_board, current_player):
  root = GameState(game_board, ' ', ' ')
  root.generate_children(current_player)
  return root

def generate_best_move(game_tree, player):
  best_move = game_tree.move

  if player == 'X':
    best_score = -999
  else:
    best_score = 999

  if game_tree.game_end == True:
    return best_move

  for game_state in game_tree.children:
    if game_state.game_end == True:
      score = game_state.score
    else:
      score = minimax(game_state, 'X' if player == 'O' else 'O')

    if player == 'X':
      if score > best_score:
        best_move = game_state.move
        best_score = score
    else:
      if score < best_score:
        best_move = game_state.move
        best_score = score

  return best_move

def minimax(game_tree, player):
  score_list = []

  if game_tree.game_end == True:
    return game_tree.score

  for game_state in game_tree.children:
    if game_state.game_end == True:
      score_list.append(game_state.score)
    else:
      game_state.score = minimax(game_state, 'X' if player == 'O' else 'O')

      #We don't need to generate the whole game tree, just return
      #the branch that will result in a win
      if player == 'X' and game_state.score == 1:
        return game_state.score
      if player == 'O' and game_state.score == -1:
        return game_state.score

      score_list.append(game_state.score)

  if player == 'X':
    return max(score_list)

  else:
    return min(score_list)