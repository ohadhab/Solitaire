import globals
import copy


def deck_click():
    if len(globals.deck) > 0:
        # print(len(globals.deck))
        globals.open_deck.append(globals.deck.pop(0))
    else:
        globals.deck = copy.deepcopy(globals.open_deck)
        globals.deck.pop(0)
        globals.open_deck = globals.open_deck = [[0, 0]]
    pass


def chose_card(i, j):
    globals.chosen_one = [i, j]
    pass


def chose_where(i, j, arranged_board):
    if globals.chosen_one == [i, j]:
        return  # cancel move
    if i > 1 and globals.chosen_one[1] == j:
        return  # cancel move
    card1, card2 = get_cards(i, j, arranged_board)
    card1[1] = reverse_names(card1[1])
    if card2 != ' ':
        card2[1] = reverse_names(card2[1])
    elif card1[1] == 13:  # check if cards is 'K' and pile is empty
        # print('moving K + topping to another pile, empty one')  # need to address the option from where is the card
        to_board(i, j, arranged_board, card1, card2)
        if globals.board[j][-1] == [' ']:
            globals.board[j].pop(-1)
        return
    else:
        return  # illegal move
    if i == 0:  # to foundations
        if arranged_board[globals.chosen_one[1]][globals.chosen_one[0] + 1] != ' ':  # check if first in pile
            return  # illegal move
        if card1[0] != card2[0] or card1[1] != card2[1] + 1:  # check if cards fit
            pass  # cards does not fit # illegal move
        else:  # move card to foundations
            to_foundations(j)
            pass
        pass
    else:  # to board (not 'K')
        do_aligned = shape_aligned(card1, card2)
        if do_aligned and card1[1] == card2[1] - 1:  # check if cards fit
            # print('moving card + topping to another pile')  # need to address the option from where is the card
            to_board(i, j, arranged_board, card1, card2)
        # elif card1[1] == 13 and arranged_board[j][i] == [' ']:  # check if cards is 'K' and pile is empty- TBD, if is OK
        #    print('moving K + topping to another pile, empty one')  # need to address the option from where is the card
        #    # can be address same as in the if?
        pass
    pass


def get_cards(i, j, arranged_board):
    card1 = arranged_board[globals.chosen_one[1]][globals.chosen_one[0]]
    card2 = arranged_board[j][i]
    return card1, card2


def reverse_names(x):
    if x == 'J':
        x = 11
    elif x == 'Q':
        x = 12
    elif x == 'K':
        x = 13
    elif x == 'A':
        x = 1
    return x


def shape_aligned(card1, card2):
    # foundations = [["Spades", 0], ["Clubs", 0], ["Diamonds", 0], ["Hearts", 0]]
    if (card1[0] in ["Spades", "Clubs"] and card2[0] in ["Spades", "Clubs"]) or (
            card1[0] in ["Diamonds", "Hearts"] and card2[0] in ["Diamonds", "Hearts"]):
        do_aligned = False
    else:
        do_aligned = True
    return do_aligned


def to_foundations(j):
    if globals.chosen_one == [0, 5]:
        card = globals.open_deck.pop(-1)
        globals.foundations[j].append(card)
    else:
        card = globals.board[globals.chosen_one[1]].pop(0)
        if len(card) > 2:
            card.pop(-1)
        if not globals.board[globals.chosen_one[1]]:
            globals.board[globals.chosen_one[1]] = [[' ']]
        globals.foundations[j].append(card)
    pass


def to_board(i, j, arranged_board, card1, card2):
    if globals.chosen_one[0] == 0:  # from foundations or open_deck
        if globals.chosen_one[1] == 5:  # from open_deck
            card = globals.open_deck.pop(-1)
            card.append('show')
            # globals.board[i-2].insert(0, card)
            globals.board[j].insert(0, card)
            pass
        else:  # from foundations
            card = globals.foundations[globals.chosen_one[1]].pop(-1)
            card.append('show')
            globals.board[j].insert(0, card)
            pass
    else:  # from board (with topping)
        no_of_card = len(globals.board[globals.chosen_one[1]]) - globals.chosen_one[0] + 2
        card = []
        for k in range(no_of_card):
            card.append(globals.board[globals.chosen_one[1]].pop(no_of_card-1-k))
            globals.board[j].insert(0, card[k])
        pass
    pass
