import copy
import globals

def solitaire_board(deck):
    # X X X X
    # left deck
    # 7 cards
    # 6 cards
    # 5 cards
    # 4 cards
    # 3 cards
    # 2 cards
    # 1 cards
    board = []
    x = 0
    for i in range(1, 7 + 1):
        col = []
        for j in range(0, i):
            col.append(deck.pop(0))
            x = x + 1
        board.append(col)
    # print("cards moved to board:" + str(x))
    board = show_noshow(board)
    # ["Spades", "Clubs", "Diamonds", "Hearts"]
    foundations = [[["Spades", 0]], [["Clubs", 0]], [["Diamonds", 0]], [["Hearts", 0]]]
    open_deck = [[0, 0]]
    return board, deck, foundations, open_deck


def show_noshow(board):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if j == 0:
                board[i][j].append("show")
            else:
                board[i][j].append("noshow")
    return board
    pass


def board_show(board):
    # board_visible = board.copy()
    board_visible = copy.deepcopy(board)
    for i in range(0, len(board_visible)):
        for j in range(0, len(board_visible[i])):
            if board_visible[i][j] == ' ' or board_visible[i][j] == [' ']:
                board_visible[i][j] = ' '
                continue
            if j == 0 and board_visible[i][j][2] == "noshow":
                board_visible[i][j][2] = "show"
                globals.board[i][j][2] = "show"
            if board_visible[i][j][2] == "noshow":
                board_visible[i][j] = ["X", "X"]
            else:
                board_visible[i][j].pop(2)
    return board_visible
