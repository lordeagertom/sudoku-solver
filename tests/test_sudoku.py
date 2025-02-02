import numpy as np
import pytest

from sudoku import Sudoku


@pytest.fixture
def empty_sudoku():
    return Sudoku()


@pytest.fixture
def solvable_sudoku():
    return Sudoku(np.array([
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


@pytest.fixture
def hard_sudoku():
    return Sudoku(np.array([
        [8, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [np.nan, np.nan, 3, 6, np.nan, np.nan, np.nan, np.nan, np.nan],
        [np.nan, 7, np.nan, np.nan, 9, np.nan, 2, np.nan, np.nan],
        [np.nan, 5, np.nan, np.nan, np.nan, 7, np.nan, np.nan, np.nan],
        [np.nan, np.nan, np.nan, np.nan, 4, 5, 7, np.nan, np.nan],
        [np.nan, np.nan, np.nan, 1, np.nan, np.nan, np.nan, 3, np.nan],
        [np.nan, np.nan, 1, np.nan, np.nan, np.nan, np.nan, 6, 8],
        [np.nan, np.nan, 8, 5, np.nan, np.nan, np.nan, 1, np.nan],
        [np.nan, 9, np.nan, np.nan, np.nan, np.nan, 4, np.nan, np.nan]
    ]))


@pytest.fixture
def unsolvable_sudoku():
    return Sudoku(np.array([
        [5, 3, np.nan, np.nan, 7, np.nan, np.nan, np.nan, np.nan],
        [6, np.nan, np.nan, 1, 9, 5, np.nan, np.nan, np.nan],
        [2, 9, 8, np.nan, np.nan, np.nan, np.nan, 6, np.nan],
        [8, np.nan, np.nan, np.nan, 6, np.nan, np.nan, np.nan, 3],
        [4, np.nan, np.nan, 8, np.nan, 3, np.nan, np.nan, 1],
        [7, np.nan, np.nan, np.nan, 2, np.nan, np.nan, np.nan, 6],
        [np.nan, 6, np.nan, np.nan, np.nan, np.nan, 2, 8, np.nan],
        [np.nan, np.nan, np.nan, 4, 1, 9, np.nan, np.nan, 5],
        [np.nan, np.nan, np.nan, np.nan, 8, np.nan, np.nan, 7, 9]
    ]))


@pytest.fixture
def complete_sudoku():
    return Sudoku(np.array([
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


@pytest.fixture
def almost_complete_sudoku():
    return Sudoku(np.array([
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, np.nan, 2, 1, 9, 5, 3, np.nan, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, np.nan, 7, 4, 1, 9, 6, np.nan, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]))


def test_default_sudoku_initialization():
    sudoku = Sudoku()
    assert sudoku.board.shape == (9, 9)


def test_sudoku_with_incorrect_board_dimensions():
    with pytest.raises(ValueError):
        invalid_board = np.zeros((8, 8))
        Sudoku(invalid_board)


def test_invalid_sudoku_cannot_be_solved():
    sudoku = Sudoku(np.array([
        [5, 5, np.nan, np.nan, 7, np.nan, np.nan, np.nan, np.nan],
        [6, np.nan, np.nan, 1, 9, 5, np.nan, np.nan, np.nan],
        [np.nan, 9, 8, np.nan, np.nan, np.nan, np.nan, 6, np.nan],
        [8, np.nan, np.nan, np.nan, 6, np.nan, np.nan, np.nan, 3],
        [4, np.nan, np.nan, 8, np.nan, 3, np.nan, np.nan, 1],
        [7, np.nan, np.nan, np.nan, 2, np.nan, np.nan, np.nan, 6],
        [np.nan, 6, np.nan, np.nan, np.nan, np.nan, 2, 8, np.nan],
        [np.nan, np.nan, np.nan, 4, 1, 9, np.nan, np.nan, 5],
        [np.nan, np.nan, np.nan, np.nan, 8, np.nan, np.nan, 7, 9]
    ]))
    assert not sudoku.solve_recursive()


def test_set_value_where_value_empty(empty_sudoku):
    empty_sudoku.set_value((5, 2), 7)
    assert empty_sudoku.board[5][2] == 7  # indices start from 0


def test_set_value_where_value_present(complete_sudoku):
    with pytest.raises(Exception):
        complete_sudoku.set_value((1, 1), 6)


@pytest.mark.parametrize("current_cell, next_cell", [
    ((0, 0), (0, 1)),
    ((0, 8), (1, 0)),
    ((8, 8), (0, 0))])
def test_move_to_next_cell(current_cell, next_cell):
    sudoku = Sudoku()
    sudoku.current_cell = current_cell
    sudoku.move_to_next_cell()
    assert sudoku.current_cell == next_cell


def test_move_to_next_cell_on_full_board(complete_sudoku):
    assert complete_sudoku.move_to_next_empty_cell() is None


@pytest.mark.parametrize("current_cell, next_empty_cell", [
    ((0, 0), (1, 1)),
    ((5, 5), (7, 1))])
def test_move_to_next_empty_cell(almost_complete_sudoku, current_cell, next_empty_cell):
    almost_complete_sudoku.current_cell = current_cell
    almost_complete_sudoku.move_to_next_empty_cell()
    assert almost_complete_sudoku.current_cell == next_empty_cell


def test_check_valid_with_empty_board(empty_sudoku):
    assert empty_sudoku.check_valid()  # Empty board is valid


def test_check_valid_with_less_than_1_value(empty_sudoku):
    empty_sudoku.set_value((2, 0), 0)
    assert not empty_sudoku.check_valid()  # This board is not valid, has values less than 1


def test_check_valid_with_greater_than_9_value(empty_sudoku):
    empty_sudoku.set_value((2, 0), 10)
    assert not empty_sudoku.check_valid()  # This board is not valid, has values greater than 9


def test_check_valid_with_nan_values(solvable_sudoku):
    assert solvable_sudoku.check_valid()  # This board is valid, gaps are filled with nan


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


def test_solve_iteratively_works_on_almost_complete_sudoku(almost_complete_sudoku):
    assert almost_complete_sudoku.solve_iterative()


@pytest.mark.parametrize("sudoku_fixture", ["solvable_sudoku", "almost_complete_sudoku", "hard_sudoku"])
def test_solve_works_on_sudoku(request, sudoku_fixture):
    sudoku = request.getfixturevalue(sudoku_fixture)
    assert sudoku.solve_recursive()  # Solvable sudoku should return True after solving


def test_solve_does_not_work_on_unsolvable_sudoku(unsolvable_sudoku):
    solved = unsolvable_sudoku.solve_recursive()
    assert not solved  # Unsolvable sudoku should return False after attempting to solve
