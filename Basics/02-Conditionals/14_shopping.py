budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram = int(input())


video_card_price = 250
bought_video_cards = number_video_cards * video_card_price
processor_price = bought_video_cards * 0.35
bought_processors = number_processors * processor_price
ram_price = bought_video_cards * 0.10
bought_rams = number_ram * ram_price

total_sum = bought_video_cards + bought_processors + bought_rams

if number_video_cards > number_processors:
    total_sum = total_sum * 0.85
else:
    pass

money_left = budget - total_sum
money_needed = total_sum - budget

if total_sum <= budget:
    print(f"You have {money_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {money_needed:.2f} leva more!")