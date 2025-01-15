import numpy as np


class Sudoku:
    def __init__(self):
        self.board = np.full((9, 9), np.nan)

    def find_next_empty_cell(self) -> tuple[int, int]:
        for i in range(9):
            for j in range(9):
                if np.isnan(self.board[i][j]):
                    return i, j

    def set_value(self, x: int, y: int, value: int):
        if not np.isnan(self.board[x][y]):
            raise ValueError(f"Can't set value {value} for cell {x}:{y}")
        self.board[x][y] = value

    def check_valid(self) -> bool:
        try:
            assert self.values_valid
            assert self.rows_valid
            assert self.columns_valid
            assert self.squares_valid
            return True
        except AssertionError:
            return False

    @property
    def values_valid(self) -> bool:
        for i in range(9):
            for j in range(9):
                if not np.isnan(self.board[i][j]):
                    if self.board[i][j] < 1 or self.board[i][j] > 9:
                        return False
        return True

    @property
    def rows_valid(self) -> bool:
        for i in range(9):
            if len(set(self.board[i][~np.isnan(self.board[i])])) != np.sum(~np.isnan(self.board[i])):
                return False
        return True

    @property
    def columns_valid(self) -> bool:
        for i in range(9):
            if len(set(self.board.T[i][~np.isnan(self.board.T[i])])) != np.sum(~np.isnan(self.board.T[i])):
                return False
        return True

    @property
    def squares_valid(self) -> bool:
        for i in range(3):
            for j in range(3):
                if len(set(self.board[3 * i:3 * i + 3, 3 * j:3 * j + 3][
                               ~np.isnan(self.board[3 * i:3 * i + 3, 3 * j:3 * j + 3])].flatten())) != np.sum(
                        ~np.isnan(self.board[3 * i:3 * i + 3, 3 * j:3 * j + 3])):
                    return False
        return True


def solve(sudoku: Sudoku):
    cell = find_next_cell(sudoku)