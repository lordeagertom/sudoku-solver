from typing import Optional

import numpy as np


class Sudoku:
    def __init__(self, board: Optional[np.ndarray] = None):
        self.board = board if board is not None else np.full((9, 9), np.nan)
        self.initial_guesses = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    @property
    def next_empty_cell(self) -> tuple[int, int]:
        for i in range(9):
            for j in range(9):
                if np.isnan(self.board[i][j]):
                    return i, j

    def set_value(self, cell: tuple[int, int], value: int):
        if not np.isnan(self.board[cell[0]][cell[1]]):
            raise ValueError(f"Can't set value {value} for cell {cell[0]}:{cell[1]}")
        self.board[cell[0]][cell[1]] = value

    def delete_value(self, cell: tuple[int, int]):
        self.board[cell[0]][cell[1]] = np.nan

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
                square_vals = self.board[3 * i:3 * i + 3, 3 * j:3 * j + 3].flatten()
                square_vals = square_vals[~np.isnan(square_vals)]
                num_cells_filled = np.sum(~np.isnan(self.board[3 * i:3 * i + 3, 3 * j:3 * j + 3]))
                if len(set(square_vals)) != num_cells_filled:
                    return False
        return True

    def solve(self) -> bool:
        solved = False
        cell = self.next_empty_cell
        guesses = self.initial_guesses
        if cell:
            while len(guesses) > 0:
                if solved:
                    return True
                self.set_value(cell, guesses[0])
                if self.check_valid():
                    solved = self.solve()
                if not solved:
                    guesses = guesses[1:]
                    self.delete_value(cell)
        else:
            return True


if __name__ == "__main__":
    sudoku = Sudoku(np.array([
        [5, 3, np.nan, np.nan, 7, np.nan, np.nan, np.nan, np.nan],
        [6, np.nan, np.nan, 1, 9, 5, np.nan, np.nan, np.nan],
        [np.nan, 9, 8, np.nan, np.nan, np.nan, np.nan, 6, np.nan],
        [8, np.nan, np.nan, np.nan, 6, np.nan, np.nan, np.nan, 3],
        [4, np.nan, np.nan, 8, np.nan, 3, np.nan, np.nan, 1],
        [7, np.nan, np.nan, np.nan, 2, np.nan, np.nan, np.nan, 6],
        [np.nan, 6, np.nan, np.nan, np.nan, np.nan, 2, 8, np.nan],
        [np.nan, np.nan, np.nan, 4, 1, 9, np.nan, np.nan, 5],
        [np.nan, np.nan, np.nan, np.nan, 8, np.nan, np.nan, 7, 9]
    ]))
    sudoku.solve()
    print(sudoku.board)
