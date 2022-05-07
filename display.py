import copy


def display_board(deck, board, foundations, open_deck):
    closed_deck = close_deck(deck)
    board2, foundations2, open_deck2 = change_names(board, foundations, open_deck)
    board_rows2 = col_to_row(board2)
    for i in range(len(foundations2)):
        print(str(foundations2[i]).ljust(19), end=" ")
    print(" ".ljust(19 + 1) + str(open_deck2[-1]).ljust(19 + 1) + str(closed_deck[-1]).ljust(19), end=" ")
    print("")
    for i in range(0, len(board_rows2)):
        print(" ")
        for j in range(len(board_rows2[i])):
            print(str(board_rows2[i][j]).ljust(19), end=" ")
    print(" ")
    pass


def col_to_row(board):
    temp = copy.deepcopy(board)
    board_rows = []
    for i in range(0, 19):
        board_rows.append([])
        for j in range(0, 7):
            board_rows[i].append([0, 0])
            if i < len(board[j]):
                board_rows[i][j] = temp[j].pop(-1)
    return board_rows
    pass


def close_deck(deck):
    closed_deck = []
    for i in range(len(deck) + 1):
        closed_deck.append(["X", "X"])
    return closed_deck


def change_names(board, foundations, open_deck):
    board2 = copy.deepcopy(board)
    foundations2 = copy.deepcopy(foundations)
    open_deck2 = copy.deepcopy(open_deck)
    for i in range(len(foundations2)):
        foundations2[i][1] = names(foundations2[i][1])
    for i in range(len(board2)):
        for j in range(len(board2[i])):
            board2[i][j][1] = names(board2[i][j][1])
    for i in range(len(open_deck2)):
        open_deck2[i][1] = names(open_deck2[i][1])
    return board2, foundations2, open_deck2


def names(x):
    if x == 11:
        x = 'J'
    elif x == 12:
        x = 'Q'
    elif x == 13:
        x = 'K'
    elif x == 1:
        x = 'A'
    return x


def arrange(deck, board, foundations, open_deck):
    arranged_board = copy.deepcopy(board)
    foundations2 = copy.deepcopy(foundations)
    for i in range(len(foundations2)):
        for j in range(len(foundations2[i])):
            if len(foundations2[i][j]) > 2:
                foundations2[i][j].pop(-1)
    if len(deck) > 0:
        x = ['X', 'X']
    else:
        x = "recycle"
    foundations2.extend([" ", [open_deck[-1]], [x]])
    for i in range(len(foundations2)):
        arranged_board[i].reverse()
        arranged_board[i] = [foundations2[i][-1], " "] + arranged_board[i]
        arranged_board[i] += [' '] * (25 - len(arranged_board[i]))
    return arranged_board
