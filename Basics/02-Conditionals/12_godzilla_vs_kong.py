budget = float(input())
number_statist = int(input())
price_clothes_p_statist = float(input())
decor = budget * 0.10
total_price_clothes = number_statist * price_clothes_p_statist

if number_statist > 150:
    total_price_clothes = total_price_clothes * 0.90

total_cost_movie = decor + total_price_clothes
total_cost = budget - total_cost_movie

money_needed = total_cost_movie - budget
money_left = budget - total_cost_movie

if total_cost_movie > budget:
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")

