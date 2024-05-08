class NQueensCSP:
    def __init__(self, board):
        self.board = board
        self.n = len(board)
        self.solutions = []

    def solve(self):
        self.place_queen(0)
        return self.solutions

    def place_queen(self, row):
        if row == self.n:
            self.solutions.append(self.board[:])
            return
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.place_queen(row + 1)
                self.board[row] = None

    def is_safe(self, row, col):
        for r in range(row):
            if (self.board[r] == col) or (self.board[r] + r == col + row) or (self.board[r] - r == col - row):
                return False
        return True

board = [
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0]
]

queen_positions = []
for row_idx, row in enumerate(board):
    for col_idx, val in enumerate(row):
        if val == 1:
            queen_positions.append(col_idx)

csp = NQueensCSP(queen_positions)
solutions = csp.solve()

if solutions:
    print("Solutions found:")
    for solution in solutions:
        for col_idx, row_idx in enumerate(solution):
            print(f"Row {col_idx + 0}, Column {row_idx + 0}")
        print()
else:
    print("No solution found.")

[1,0,0,0,0]
[0,0,0,1,0]
[0,1,0,0,0]
[0,0,0,0,1]
[0,0,1,0,0]