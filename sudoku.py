from typing import Optional

import numpy as np


class Sudoku:
    def __init__(self, board: Optional[np.ndarray] = None):
        if board is not None:
            if board.shape != (9, 9):
                raise ValueError("The board must be of shape 9x9")
            self.board = board
        else:
            self.board = np.full((9, 9), np.nan)
        self.current_cell = (0, 0)
        self.cell_options = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        if not self.check_valid():
            raise ValueError("The board is not valid")

    def check_valid(self) -> bool:
        try:
            assert self.values_valid  # checks that no values outside the 1-9 range are present in the puzzle
            assert self.rows_valid  # checks that there are no row conflicts
            assert self.columns_valid  # checks that there are no column conflicts
            assert self.squares_valid  # checks that there are no square conflicts
            return True
        except AssertionError:
            return False

    def move_to_next_cell(self):
        if self.current_cell[1] < 8:
            self.current_cell = (self.current_cell[0], self.current_cell[1] + 1)
        elif self.current_cell[0] < 8:
            self.current_cell = (self.current_cell[0] + 1, 0)
        else:
            if not np.isnan(self.board).any():
                self.current_cell = None
            else:
                self.current_cell = (0, 0)
        return self.current_cell

    def set_value(self, cell: tuple[int, int], value: int):
        if not np.isnan(self.board[cell[0]][cell[1]]):
            raise ValueError(f"Can't set value {value} for cell {cell[0]}:{cell[1]}")
        self.board[cell[0]][cell[1]] = value
        return self.check_valid()

    def solve_iterative(self) -> bool:
        while self.move_to_next_cell():
            options = [x for x in self.cell_options if x not in self.find_disallowed_values()]
            if len(options) == 1:
                self.set_value(self.current_cell, options[0])
        return True

    def find_disallowed_values(self):
        row = self.board[self.current_cell[0], :]
        col = self.board[:, self.current_cell[1]]
        square = self.board[3 * (self.current_cell[0] // 3):3 * (self.current_cell[0] // 3) + 3,
                 3 * (self.current_cell[1] // 3):3 * (self.current_cell[1] // 3) + 3]
        disallowed_values = np.unique(np.concatenate([row, col, square.ravel()]))
        return disallowed_values[~np.isnan(disallowed_values)]

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

    def move_to_next_empty_cell(self):
        while self.current_cell is not None and not np.isnan(self.board[self.current_cell]):
            self.move_to_next_cell()
        return self.current_cell

    def solve_recursive(self) -> bool:
        if not self.move_to_next_empty_cell():  # there are no remaining empty cells i.e. the sudoku has been solved
            return True

        for guess in self.cell_options:
            sudoku = Sudoku(board=self.board.copy())
            if sudoku.set_value(self.current_cell, guess):
                if sudoku.solve_recursive():
                    return True

        return False  # if we try all options for a cell


if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.solve_iterative()
    print(sudoku.board)
