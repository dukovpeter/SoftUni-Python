price_travel = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

puzzles_price = 2.60
dolls_price = 3
bears_price = 4.1
minions_price = 8.2
trucks_price = 2
discount = 0

ordered_items = number_puzzles + number_dolls + number_bears + number_minions + number_trucks
total_price = (number_puzzles * puzzles_price) + (number_dolls * dolls_price) + (number_bears * bears_price) + (number_minions * minions_price) + (number_trucks * trucks_price)

if ordered_items >= 50:
    total_price = total_price * 0.75
else:
    discount = 0.00

rent = total_price * 0.10
profit = total_price - rent
left_money = profit - price_travel
needed_money = price_travel - profit

if profit >= price_travel:
    print(f"Yes! {left_money:.2f} lv left.")
else:
    print(f"Not enough money! {needed_money:.2f} lv needed.")