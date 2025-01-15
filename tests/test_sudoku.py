import numpy as np
import pytest
from sudoku import Sudoku


@pytest.fixture
def empty_sudoku():
    return Sudoku()


@pytest.fixture
def partial_sudoku():
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
    return sudoku


@pytest.fixture
def complete_sudoku():
    sudoku = Sudoku(np.array([
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]))
    return sudoku


def test_set_value_where_value_empty(empty_sudoku):
    empty_sudoku.set_value((5, 2), 7)
    assert empty_sudoku.board[5][2] == 7  # indices start from 0


def test_set_value_where_value_present(complete_sudoku):
    with pytest.raises(Exception):
        complete_sudoku.set_value(0, 6)


def test_delete_value():
    sudoku = Sudoku()
    sudoku.set_value((0, 0), 5)
    sudoku.delete_value((0, 0))

    assert np.isnan(sudoku.board[0][0]), "The value at the specified position was not deleted properly"


def test_check_valid_with_empty_board(empty_sudoku):
    assert empty_sudoku.check_valid()  # Empty board is valid


def test_check_valid_with_less_than_1_value(empty_sudoku):
    empty_sudoku.set_value((2, 0), 0)
    assert not empty_sudoku.check_valid()  # This board is not valid, has values less than 1


def test_check_valid_with_greater_than_9_value(empty_sudoku):
    empty_sudoku.set_value((2, 0), 10)
    assert not empty_sudoku.check_valid()  # This board is not valid, has values greater than 9


def test_check_valid_with_nan_values(partial_sudoku):
    assert partial_sudoku.check_valid()  # This board is valid, gaps are filled with nan


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


def test_find_next_cell_on_empty_board(empty_sudoku):
    assert empty_sudoku.find_next_empty_cell() == (0, 0)  # First cell should be (0, 0)


def test_find_next_cell_on_partially_filled_board(partial_sudoku):
    assert partial_sudoku.find_next_empty_cell() == (0, 2)  # First empty cell should be (0, 2)


def test_find_next_cell_on_full_board(complete_sudoku):
    assert complete_sudoku.find_next_empty_cell() is None


def test_check_complete_on_full_board(complete_sudoku):
    assert complete_sudoku.complete  # Complete board should be marked as complete


def test_check_complete_on_partially_filled_board(partial_sudoku):
    assert not partial_sudoku.complete  # Partially filled board should not be marked as complete
