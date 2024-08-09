# List misc operations
def test_board():
    board = [["_"] * 3 for _ in range(3)]
    assert board == [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    board[0][0] = "x"
    assert board == [["x", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    board[1][1] = "o"
    assert board == [["x", "_", "_"], ["_", "o", "_"], ["_", "_", "_"]]


def test_board_v2():
    board = [["_"] * 3] * 3
    assert board == [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    board[0][0] = "x"
    assert board == [["x", "_", "_"], ["x", "_", "_"], ["x", "_", "_"]]


def test_operators():
    lst = [1, 2, 3]
    lst += [4, 5]
    assert lst == [1, 2, 3, 4, 5]
    lst *= 2
    assert lst == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
