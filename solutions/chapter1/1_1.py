board = [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]

player = "x"


def switch():
    global player
    if player == "x":
        player = "o"
    else:
        player = "x"


def pboard():
    for row in board:
        print("|".join(row))


def marker(x: int, y: int):
    global player
    board[x - 1][y - 1] = f" {player} "
    switch()
    pboard()
