import tkinter
import display
import globals
import board as board_functions
import game
import copy


def onclick(i, j, b, arranged_board):
    if i == 0 and j == 6:
        # card from deck
        game.deck_click()
        globals.first_click = True
        pass
    elif globals.first_click:
        # chose card to move
        game.chose_card(i, j)
        # tkinter.messagebox.showinfo("Hello Python", "Hello World " + str(i) + " " + str(j) + str(globals.first_click))
        b[i][j]['bg'] = 'yellow'
        globals.first_click = False
    else:
        # chose where to move
        game.chose_where(i, j, arranged_board)
        # tkinter.messagebox.showinfo("Hello Python", "Hello World " + str(i) + " " + str(j) + str(globals.first_click))
        globals.first_click = True
    gui_update(b)


def gui_make(win, arranged_board):
    buttons = []
    # win = tkinter.Tk()
    win.title("Solitaire")
    win.geometry()
    frame = tkinter.Frame(win)
    frame.pack()
    b = []
    spacer1 = tkinter.Label(frame, text=" ", height=1, width=10)
    spacer2 = tkinter.Label(frame, text=" ", height=1, width=10)
    for i in range(25):
        b.append([])
        if i == 1:
            spacer1.grid(row=i, column=0)
            continue
        for j in range(7):
            if arranged_board[j][i] != " ":
                arranged_board[j][i][1] = display.names(arranged_board[j][i][1])
            b[i].append([])
            if arranged_board[j][i] == " " and i != 2:
                # spacer2.grid(row=i, column=j)
                b[i][j] = tkinter.Button(frame, fg='black', text=' ', height=1, width=12, state='disable',
                                         command=lambda i=i, j=j: onclick(i, j, b, globals.arranged_board2))
                b[i][j].grid(row=i, column=j)
                b[i][j]['bd'] = 0
                continue
            # b[i][j] = tkinter.Button(frame, fg="red", text=(str(i) + " " + str(j)), state="disabled", height=1, width=10, command=lambda i=i, j=j: onClick(i, j))
            # b[i][j] = tkinter.Button(frame, fg="red", text=(str(i) + " " + str(j)), height=1, width=10, command=lambda i=i, j=j: onClick(i, j))
            if arranged_board[j][i][0] == "Diamonds" or arranged_board[j][i][0] == "Hearts":
                fg = "red"
            else:
                fg = "black"
            textt = suit_symbols(arranged_board[j][i])
            x = copy.deepcopy(arranged_board[j][i])
            if textt != None:
                x.append(textt)
            #b[i][j] = tkinter.Button(frame, fg=fg, text=(arranged_board[j][i]), height=1, width=10,
            #                        command=lambda i=i, j=j: onclick(i, j, b, globals.arranged_board2))
            b[i][j] = tkinter.Button(frame, fg=fg, text=(x), height=1, width=12,
                                    command=lambda i=i, j=j: onclick(i, j, b, globals.arranged_board2))
            b[i][j].grid(row=i, column=j)
            if (i != 0) and arranged_board[j][i] == ['X', 'X']:
                b[i][j]['state'] = "disabled"
            elif i == 0 and arranged_board[j][i] == [0, 0]:
                b[i][j]['text'] = 'empty'
                b[i][j]['state'] = "disabled"
            # elif i == 0 and arranged_board[j][i][1] == 0 and globals.first_click:
            elif arranged_board[j][i][1] == 0 and globals.first_click:
                b[i][j]['state'] = "disabled"
            elif i == 2 and arranged_board[j][i] == ' ' and globals.first_click:
                b[i][j]['text'] = 'empty'
                b[i][j]['state'] = "disabled"
            else:
                b[i][j]['state'] = "normal"
            buttons.append(b[i])
    # TBD add photos
    # photo = tkinter.PhotoImage(file=r"C:\python_projects\solitaire\cards\2_of_clubs.png", master=win)
    # b[2][0]['image'] = photo
    # spacer2 = tkinter.Label(frame, text=" ", height=1, width=10)
    # spacer2.image = photo
    # spacer2.config(image=photo)
    # spacer2.grid(row=0, column=5)
    return


def gui_update(b):
    board_visible = board_functions.board_show(globals.board)
    arranged_board = display.arrange(globals.deck, board_visible, globals.foundations, globals.open_deck)
    globals.arranged_board2 = arranged_board
    for i in range(25):
        for j in range(7):
            if globals.first_click:
                if arranged_board[j][i] != "recycle":
                    if arranged_board[j][i] != " ":
                        arranged_board[j][i][1] = display.names(arranged_board[j][i][1])
                    if arranged_board[j][i][0] == "Diamonds" or arranged_board[j][i][0] == "Hearts":
                        fg = "red"
                    else:
                        fg = "black"
                    textt = suit_symbols(arranged_board[j][i])
                    x = copy.deepcopy(arranged_board[j][i])
                    if textt != None:
                        x.append(textt)
                    if i == 1:
                        continue
                    if arranged_board[j][i] == " " and i != 2:
                        b[i][j]['text'] = " "
                        b[i][j]['state'] = "disabled"
                        b[i][j]['bg'] = 'SystemButtonFace'
                        b[i][j]['bd'] = 0
                        continue
                    b[i][j]['text'] = x
                else:
                    fg = "black"
                    b[i][j]['text'] = arranged_board[j][i]
                #b[i][j]['text'] = arranged_board[j][i]
                b[i][j]['fg'] = fg
                b[i][j]['bg'] = 'SystemButtonFace'
                b[i][j]['bd'] = 2
            if i == 1:
                continue
            if i == 2 and arranged_board[j][i] == ' ':
                if globals.first_click:
                    b[i][j]['text'] = 'empty'
                    b[i][j]['state'] = "disabled"
                else:
                    b[i][j]['state'] = "active"
            if arranged_board[j][i] == " ":
                continue
            if (i != 0) and arranged_board[j][i] == ['X', 'X']:
                b[i][j]['state'] = "disabled"
            elif i == 0 and arranged_board[j][i] == [0, 0]:
                b[i][j]['text'] = 'empty'
                b[i][j]['state'] = "disabled"
                # elif i == 0 and arranged_board[j][i][1] == 0 and globals.first_click:
            elif arranged_board[j][i][1] == 0 and globals.first_click:
                b[i][j]['state'] = "disabled"
            elif i == 0 and j == 5 and b[i][j]['bg'] != 'yellow' and not globals.first_click:
                b[i][j]['state'] = "disabled"
            elif i == 2 and arranged_board[j][i] == ' ' and globals.first_click:
                b[i][j]['text'] = 'empty'
                b[i][j]['state'] = "disabled"
            else:
                b[i][j]['state'] = "normal"


def suit_symbols(card):
    if len(card) != 2 or card[0] not in ["Spades", "Clubs", "Diamonds", "Hearts"]:
        return None
    sy = {
        'Spades': u'♠',
        'Diamonds': u'♦',
        'Clubs': u'♣',
        'Hearts': u'♥',
    }
    # ["Spades", "Clubs", "Diamonds", "Hearts"]
    x = sy[card[0]]
    return x
