from typing import Optional

import numpy as np


class Sudoku:
    def __init__(self, board: Optional[np.ndarray] = None):
        self.board = board if board is not None else np.full((9, 9), np.nan)
        self.current_cell = (0, 0)

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
                if len(set(self.board[3 * i:3 * i + 3, 3 * j:3 * j + 3][
                               ~np.isnan(self.board[3 * i:3 * i + 3, 3 * j:3 * j + 3])].flatten())) != np.sum(
                    ~np.isnan(self.board[3 * i:3 * i + 3, 3 * j:3 * j + 3])):
                    return False
        return True


if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.solve()
    print(sudoku.board)
