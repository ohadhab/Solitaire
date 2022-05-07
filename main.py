from tkinter import PhotoImage, Label, Button

import deck_functions
import board as board_functions
import display
import tkinter.messagebox
import gui
import globals

globals.initialize()

# import tkMessageBox
# global click_no
# click_no = bool(0)

# deck = deck_functions.create_card_deck()
globals.deck = deck_functions.create_card_deck()

# deck = deck_functions.shuffle_deck(deck)
globals.deck = deck_functions.shuffle_deck(globals.deck)

# board, deck, foundations, open_deck = board_functions.solitaire_board(deck)
globals.board, globals.deck, globals.foundations, globals.open_deck = board_functions.solitaire_board(globals.deck)

board_visible = board_functions.board_show(globals.board)

# display.display_board(deck, board_visible, foundations, open_deck)
# arranged_board = display.arrange(deck, board_visible, foundations, open_deck)
arranged_board = display.arrange(globals.deck, board_visible, globals.foundations, globals.open_deck)
globals.arranged_board2 = arranged_board

win = tkinter.Tk()
gui.gui_make(win, arranged_board)

win.mainloop()
