import sudoku_logic


def test_create_empty_board_has_9_by_9_grid():
    board = sudoku_logic.create_empty_board()

    assert len(board) == 9
    assert all(len(row) == 9 for row in board)
    assert all(cell == sudoku_logic.EMPTY for row in board for cell in row)


def test_is_safe_detects_conflicts_in_row_column_and_box():
    board = sudoku_logic.create_empty_board()
    board[0][0] = 5

    assert sudoku_logic.is_safe(board, 0, 1, 5) is False
    assert sudoku_logic.is_safe(board, 1, 0, 5) is False
    assert sudoku_logic.is_safe(board, 2, 2, 5) is False
    assert sudoku_logic.is_safe(board, 2, 3, 5) is True


def test_generate_puzzle_returns_valid_9x9_puzzle_and_solution():
    puzzle, solution = sudoku_logic.generate_puzzle(35)

    assert len(puzzle) == 9
    assert len(solution) == 9
    assert all(len(row) == 9 for row in puzzle)
    assert all(len(row) == 9 for row in solution)
    assert any(cell == 0 for row in puzzle for cell in row)

    for row in solution:
        assert sorted(row) == list(range(1, 10))

    for row in range(sudoku_logic.SIZE):
        for col in range(sudoku_logic.SIZE):
            value = puzzle[row][col]
            assert value in range(0, 10)
            if value != 0:
                assert value == solution[row][col]

    for row in range(sudoku_logic.SIZE):
        values = [solution[row][col] for col in range(sudoku_logic.SIZE)]
        assert sorted(values) == list(range(1, 10))

    for col in range(sudoku_logic.SIZE):
        values = [solution[row][col] for row in range(sudoku_logic.SIZE)]
        assert sorted(values) == list(range(1, 10))

    for box_row in range(0, sudoku_logic.SIZE, 3):
        for box_col in range(0, sudoku_logic.SIZE, 3):
            values = []
            for row in range(box_row, box_row + 3):
                for col in range(box_col, box_col + 3):
                    values.append(solution[row][col])
            assert sorted(values) == list(range(1, 10))
