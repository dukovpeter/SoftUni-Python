from math import ceil

product = input("")
town = input("")
quantity = float(input())
price = 0
total_price = 0

if town == "Sofia":
    if product == "coffee":
        price = 0.50
        total_price = price * quantity
    elif product == "water":
        price = 0.80
        total_price = price * quantity
    elif product == "beer":
        price = 1.20
        total_price = price * quantity
    elif product == "sweets":
        price = 1.45
        total_price = price * quantity
    elif product == "peanuts":
        price = 1.60
        total_price = price * quantity
elif town == "Plovdiv":
    if product == "coffee":
        price = 0.40
        total_price = price * quantity
    elif product == "water":
        price = 0.70
        total_price = price * quantity
    elif product == "beer":
        price = 1.15
        total_price = price * quantity
    elif product == "sweets":
        price = 1.30
        total_price = price * quantity
    elif product == "peanuts":
        price = 1.50
        total_price = price * quantity
elif town == "Varna":
    if product == "coffee":
        price = 0.45
        total_price = price * quantity
    elif product == "water":
        price = 0.70
        total_price = price * quantity
    elif product == "beer":
        price = 1.10
        total_price = price * quantity
    elif product == "sweets":
        price = 1.35
        total_price = price * quantity
    elif product == "peanuts":
        price = 1.55
        total_price = price * quantity

print(total_price)
