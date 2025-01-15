import pytest
import numpy as np
from sudoku import Sudoku


def test_set_value():
    sudoku = Sudoku()
    sudoku.set_value(5, 2, 7)
    assert sudoku.board[4][1] == 7  # indices start from 0


def test_check_valid_with_empty_board():
    sudoku = Sudoku()
    assert sudoku.check_valid()  # Empty board is valid


def test_check_valid_with_less_than_1_value():
    sudoku = Sudoku()
    sudoku.board = np.array([
        [5, 3, np.nan, np.nan, 7, np.nan, np.nan, np.nan, np.nan],
        [6, np.nan, np.nan, 1, 9, 5, np.nan, np.nan, np.nan],
        [np.nan, 9, 8, np.nan, np.nan, np.nan, np.nan, 6, np.nan],
        [8, np.nan, np.nan, np.nan, 6, np.nan, np.nan, np.nan, 3],
        [4, np.nan, np.nan, 8, 0, 3, np.nan, np.nan, 1],
        [7, np.nan, np.nan, np.nan, 2, np.nan, np.nan, np.nan, 6],
        [np.nan, 6, np.nan, np.nan, np.nan, np.nan, 2, 8, np.nan],
        [np.nan, np.nan, np.nan, 4, 1, 9, np.nan, np.nan, 5],
        [np.nan, np.nan, np.nan, np.nan, 8, np.nan, np.nan, 7, 9]
    ])
    assert not sudoku.check_valid()  # This board is not valid, has values less than 1


def test_check_valid_with_greater_than_9_value():
    sudoku = Sudoku()
    sudoku.board = np.array([
        [5, 3, np.nan, np.nan, 7, np.nan, np.nan, np.nan, np.nan],
        [6, np.nan, np.nan, 1, 9, 5, np.nan, np.nan, 10],
        [np.nan, 9, 8, np.nan, np.nan, np.nan, np.nan, 6, np.nan],
        [8, np.nan, np.nan, np.nan, 6, np.nan, np.nan, np.nan, 3],
        [4, np.nan, np.nan, 8, np.nan, 3, np.nan, np.nan, 1],
        [7, np.nan, np.nan, np.nan, 2, np.nan, np.nan, np.nan, 6],
        [np.nan, 6, np.nan, np.nan, np.nan, np.nan, 2, 8, np.nan],
        [np.nan, np.nan, np.nan, 4, 1, 9, np.nan, np.nan, 5],
        [np.nan, np.nan, np.nan, np.nan, 8, np.nan, np.nan, 7, 9]
    ])
    assert not sudoku.check_valid()  # This board is not valid, has values greater than 9


def test_check_valid_with_nan_values():
    sudoku = Sudoku()
    sudoku.board = np.array([
        [5, 3, np.nan, np.nan, 7, np.nan, np.nan, np.nan, np.nan],
        [6, np.nan, np.nan, 1, 9, 5, np.nan, np.nan, np.nan],
        [np.nan, 9, 8, np.nan, np.nan, np.nan, np.nan, 6, np.nan],
        [8, np.nan, np.nan, np.nan, 6, np.nan, np.nan, np.nan, 3],
        [4, np.nan, np.nan, 8, np.nan, 3, np.nan, np.nan, 1],
        [7, np.nan, np.nan, np.nan, 2, np.nan, np.nan, np.nan, 6],
        [np.nan, 6, np.nan, np.nan, np.nan, np.nan, 2, 8, np.nan],
        [np.nan, np.nan, np.nan, 4, 1, 9, np.nan, np.nan, 5],
        [np.nan, np.nan, np.nan, np.nan, 8, np.nan, np.nan, 7, 9]
    ])
    assert sudoku.check_valid()  # This board is valid, gaps are filled with nan


def test_rows_valid_with_invalid_row():
    sudoku = Sudoku()
    sudoku.board[0] = np.array([1, 1, 3, 4, 5, 6, 7, 8, 9])  # Invalid row with repeated number
    assert not sudoku.rows_valid


def test_columns_valid_with_invalid_column():
    sudoku = Sudoku()
    sudoku.board[:, 0] = np.array([1, 1, 3, 4, 5, 6, 7, 8, 9])  # Invalid column with repeated number
    assert not sudoku.columns_valid


def test_squares_valid_with_invalid_square():
    sudoku = Sudoku()
    sudoku.board[0:3, 0:3] = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 1, 9]  # Invalid square with repeated number
    ])
    assert not sudoku.squares_valid
