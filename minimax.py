class TicTacToe:
    def __init__(self, board):
        self.board = board

    # Function to check for winner
    def is_winner(self, player):
        # Check rows
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                return True

        # Check columns
        for j in range(3):
            if all(self.board[i][j] == player for i in range(3)):
                return True

        # Check main diagonal
        if all(self.board[i][i] == player for i in range(3)):
            return True

        # Check secondary diagonal
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    # Function to update board after inserting children
    def insert_child(self, player):
        children = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    dup_board = [row[:] for row in self.board]
                    dup_board[i][j] = player
                    children.append((TicTacToe(dup_board), (i,j)))
        return children

    # Function to check if the game is drawn
    def is_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    return False
        return True

    # Function to check if the game is terminated
    def is_terminal(self):
        return self.is_winner('x') or self.is_winner('o') or self.is_draw()

    # Minimax algorithm
    def minimax(self, node, depth, maximizingPlayer):
          if depth == 0 or node.is_terminal():
               return node.static_evaluation(), None
          best_move = None
          if maximizingPlayer:  # Maximizing player's turn
               maxEva = float('-inf')
               for child, move in node.insert_child('x'):
                    eva, _ = self.minimax(child, depth - 1, False)
                    if eva > maxEva:
                         maxEva = eva
                         best_move = move
               return maxEva, best_move
          else:  # Minimizing player's turn
               minEva = float('inf')
               for child, move in node.insert_child('o'):
                    eva, _ = self.minimax(child, depth - 1, True)
                    if eva < minEva:
                         minEva = eva
                         best_move = move
               return minEva, best_move


    # Static evaluation function
    def static_evaluation(self):
        if self.is_winner('x'):
            return 10
        elif self.is_winner('o'):
            return -10
        elif self.is_draw():
            return 0
        else:
            return 0

# Sample board
board = [
    ['x', 'x', 'o'],
    ['x', '', 'o'],
    ['o', 'o', '']
]

# Create the root node
root_node = TicTacToe(board)

# Call minimax function to find the best move
depth = 3
maximizingPlayer = True
alpha = float('-inf')
beta = float('inf')
best_score,best_move = root_node.minimax(root_node, depth,maximizingPlayer)
print("Best Score:", best_score)
print("Best Move:", best_move)
