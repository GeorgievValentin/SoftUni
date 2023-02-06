deck = input().split()
shuffles = int(input())
half = int(len(deck) / 2)
left_cards = []
right_cards = []

for shuffle in range(shuffles):
    current_deck = []
    left_cards = deck[:half]
    right_cards = deck[half::]
    for card_index in range(len(left_cards)):
        current_deck.append(left_cards[card_index])
        current_deck.append(right_cards[card_index])
    deck = current_deck
print(deck)
