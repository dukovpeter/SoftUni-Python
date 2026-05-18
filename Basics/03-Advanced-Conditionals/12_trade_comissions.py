city = input()
sales = float(input())

if sales < 0:
    print("error")
    exit()

discount = 0

if city == "Sofia":
    if sales <= 500:
        discount = 0.05
    elif sales <= 1000:
        discount = 0.07
    elif sales <= 10000:
        discount = 0.08
    else:
        discount = 0.12

elif city == "Varna":
    if sales <= 500:
        discount = 0.045
    elif sales <= 1000:
        discount = 0.075
    elif sales <= 10000:
        discount = 0.10
    else:
        discount = 0.13

elif city == "Plovdiv":
    if sales <= 500:
        discount = 0.055
    elif sales <= 1000:
        discount = 0.08
    elif sales <= 10000:
        discount = 0.12
    else:
        discount = 0.145

else:
    print("error")
    exit()

merchant_commission = sales * discount
print(f"{merchant_commission:.2f}")