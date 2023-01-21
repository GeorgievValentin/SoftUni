budget = float(input())
video_cards = int(input())
processors = int(input())
memories = int(input())

video_card_price = 250
processor_price = video_cards * video_card_price * 0.35
memory_price = video_cards * video_card_price * 0.1
cost = video_cards * video_card_price + processors * processor_price + memories * memory_price

if video_cards > processors:
    cost *= 0.85
diff = abs(budget - cost)
if budget >= cost:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")