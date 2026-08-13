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
def test_solved_board_has_exactly_one_solution():
    board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]

    assert sudoku_logic.count_solutions(board, limit=2) == 1


def test_empty_board_has_more_than_one_solution():
    board = sudoku_logic.create_empty_board()

    assert sudoku_logic.count_solutions(board, limit=2) > 1


def test_generate_puzzle_has_exactly_one_solution():
    puzzle, _ = sudoku_logic.generate_puzzle(35)

    assert sudoku_logic.count_solutions(puzzle, limit=2) == 1


def test_generated_solution_is_valid():
    puzzle, solution = sudoku_logic.generate_puzzle(35)

    assert len(solution) == sudoku_logic.SIZE
    assert all(len(row) == sudoku_logic.SIZE for row in solution)

    for row in solution:
        assert sorted(row) == list(range(1, sudoku_logic.SIZE + 1))

    for col in range(sudoku_logic.SIZE):
        values = [solution[row][col] for row in range(sudoku_logic.SIZE)]
        assert sorted(values) == list(range(1, sudoku_logic.SIZE + 1))

    for box_row in range(0, sudoku_logic.SIZE, 3):
        for box_col in range(0, sudoku_logic.SIZE, 3):
            values = []
            for row in range(box_row, box_row + 3):
                for col in range(box_col, box_col + 3):
                    values.append(solution[row][col])
            assert sorted(values) == list(range(1, sudoku_logic.SIZE + 1))

    for row in range(sudoku_logic.SIZE):
        for col in range(sudoku_logic.SIZE):
            if puzzle[row][col] != sudoku_logic.EMPTY:
                assert puzzle[row][col] == solution[row][col]