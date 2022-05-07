from random import shuffle


def create_card_deck():
    suite = ["Spades", "Clubs", "Diamonds", "Hearts"]
    # print(suite)
    value = list(range(1, 13 + 1))
    # print(value)
    deck = []
    for i in suite:
        for j in value:
            deck.append([i, j])
    # print(len(deck))
    return deck
    pass


def shuffle_deck(deck):
    shuffle(deck)
    return deck
    pass
