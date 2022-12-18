import random
# ----------------------------------------------------------------------------
# 1. Deck setup
#      * Deck contains 32 cards from 3 to 35 inclusive.
#      * Before the game begins, 9 cards are removed at random.
deck = list(range(3, 36))
remove_cards = random.sample(range(3, 36), 9)

for card in remove_cards:
    deck.remove(card)


# ----------------------------------------------------------------------------
# 2A. Player strategies
#      * Naive: player just accepts whatever card they're given
#      * Low cards: player won't accept high valued (n > 25) cards unless
#        they run out of counters.
#      * Counters: player will accept any card that has counters greater
#        than two, otherwise pass the card around - unless the card is n > 13
#      * Sequential: player will accept low value cards (n < 15) but will
#        make moves for cards that complete a sequential set that brings the
#        score down.
def naive(player, current_card):
    player["cards"].append(current_card)
    print("{0} is being naive and accepts the current card.".format(player["name"]))


def low_cards(player, current_card):
    print("{0} is only interested in cards less than 25.".format(player["name"]))
    pass


def counter_collection(player, current_card):
    print("{0} only wants cards less than 13 or any card with more than two counters on it.".format(player["name"]))
    pass


def sequential_cards(player, current_card):
    print("{0} is looking for cards that run in sequential order to his.".format(player["name"]))
    pass


# ----------------------------------------------------------------------------
# 2B. Player setup
#      * Each player has 11 counters at the start, and no cards.
players = [
    {
        "id": 1,
        "name": "Alice",
        "cards": list(),
        "counters": 11,
        "strategy": naive
    },
    {
        "id": 2,
        "name": "Bob",
        "cards": list(),
        "counters": 11,
        "strategy": low_cards
    },
    {
        "id": 3,
        "name": "Carol",
        "cards": list(),
        "counters": 11,
        "strategy": counter_collection
    },
    {
        "id": 4,
        "name": "Dave",
        "cards": list(),
        "counters": 11,
        "strategy": sequential_cards
    },
]



# ----------------------------------------------------------------------------
# 3. Start Game
#      * Each player gets a turn, starting with player 1
#
active_player = 1

while len(deck) > 0:
    # Active player index
    active_player_index = active_player - 1

    # Select a card and remove it. That is the card up for debate
    # amongst the players.
    current_card = random.choice(deck)
    deck.remove(current_card)

    while card_is_in_play:
    # Use the players strategy
    players[active_player_index]["strategy"](players[active_player_index], current_card)

    # End turn and constrain the loop to four players.
    active_player = active_player + 1
    if active_player % 4 == 1:
        active_player = 1

# ----------------------------------------------------------------------------
# 4. Game is now over, calculate the scores
#
for player in players:
    print("{0} (Player {1}) has a score of {2}".format(
        player["name"],
        player["id"],
        sum(player["cards"]) - player["counters"]
    ))
