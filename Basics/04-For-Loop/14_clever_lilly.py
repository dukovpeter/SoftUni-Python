lilly_age = int(input())
x = float(input())
price_for_toy = int(input())

money_saved = 0
toys_counter = 0
money_gift = 10


for age in range(1, lilly_age + 1):
    if age % 2 == 0:
        money_saved += money_gift
        money_gift += 10
        money_saved -= 1
    else:
        toys_counter += 1

money_saved += toys_counter * price_for_toy
diff = abs(money_saved - x)

if money_saved >= x:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")