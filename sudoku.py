import numpy as np


class Sudoku:
    def __init__(self):
        self.board = [[np.nan for _ in range(9)] for _ in range(9)]

    def set(self, x, y, value):
        self.board[x][y] = value

