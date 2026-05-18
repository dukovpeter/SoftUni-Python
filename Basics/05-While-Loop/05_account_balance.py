new_input = input()
total_money = 0.0

while new_input != "NoMoreMoney":
    deposit = float(new_input)
    if deposit < 0:
        print("Invalid operation!")
        break
    print(f" Increase: {deposit:.2f} ")

    total_money += deposit
    new_input = input()

print(f"Total: {total_money:.2f} ")
