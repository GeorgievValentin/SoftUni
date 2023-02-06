red_cards = input().split()
set_cards = set(red_cards)
terminated = False
a_players = 11
b_players = 11

for card in set_cards:
    if "A" in card:
        a_players -= 1
    elif "B" in card:
        b_players -= 1
    if a_players < 7 or b_players < 7:
        terminated = True
        break
print(f"Team A - {a_players}; Team B - {b_players}")
if terminated:
    print("Game was terminated")
