budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price_per_liter = flour_price * 1.25
milk_price_for_one_bread = milk_price_per_liter * 0.250

bread_price = flour_price + eggs_price + milk_price_for_one_bread

bread_count = 0
colored_eggs = 0

while budget >= bread_price:
    budget -= bread_price
    bread_count += 1
    colored_eggs += 3

    if bread_count % 3 == 0:
        colored_eggs -= bread_count - 2

print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")