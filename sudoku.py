from typing import Optional

import numpy as np


class Sudoku:
    def __init__(self, board: Optional[np.ndarray] = None):
        if board is not None:
            if board.shape != (9, 9):
                raise ValueError("The board must be of shape 9x9")
            self.board = board
            if not self.check_valid():
                raise ValueError("The board is already not valid as initialised")
        else:
            self.board = np.full((9, 9), np.nan)
        self.current_cell = (0, 0)
        self.initial_guesses = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    def move_to_next_cell(self):
        cell = self.current_cell
        if cell[0] < 8:
            self.current_cell = (cell[0] + 1, cell[1])
        elif cell[1] < 8:
            self.current_cell = (0, cell[1] + 1)
        else:
            self.current_cell = (0, 0)

    def set_value(self, cell: tuple[int, int], value: int):
        if not np.isnan(self.board[cell[0]][cell[1]]):
            raise ValueError(f"Can't set value {value} for cell {cell[0]}:{cell[1]}")
        self.board[cell[0]][cell[1]] = value

    def solve_iterative(self) -> bool:
        solved = False
        while not solved:
            cell = self.current_cell
            if np.isnan(self.board[cell[0]][cell[1]]):
                options = list(self.initial_guesses)
                row = self.board[cell[0], :]
                col = self.board[:, cell[1]]
                square = self.board[3 * (cell[0] // 3):3 * (cell[0] // 3) + 3, 3 * (cell[1] // 3):3 * (cell[1] // 3) + 3]
                for element in np.unique(np.concatenate([row, col, square.ravel()])):
                    try:
                        options.remove(element)
                    except ValueError:
                        pass
                if len(options) == 1:
                    self.set_value(cell, options[0])
            if not np.isnan(self.board).any():
                solved = True
            self.move_to_next_cell()
        return solved

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
    def next_empty_cell(self) -> tuple[int, int]:
        for i in range(9):
            for j in range(9):
                if np.isnan(self.board[i][j]):
                    return i, j

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

    def solve_recursive(self) -> bool:
        solved = False
        cell = self.next_empty_cell
        guesses = self.initial_guesses
        if cell:
            while len(guesses) > 0:
                if solved:
                    return True
                self.set_value(cell, guesses[0])
                if self.check_valid():
                    solved = self.solve_recursive()
                if not solved:
                    guesses = guesses[1:]
                    self.delete_value(cell)
        else:
            return True


if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.solve_iterative()
    print(sudoku.board)
