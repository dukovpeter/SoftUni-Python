needed_money = float(input())
available_money = float(input())
counter_spend = 0
days_passed = 0


while available_money < needed_money and counter_spend < 5:
    action = input()
    amount = float(input())
    days_passed += 1

    if action == "spend":
        available_money -= amount
        counter_spend += 1

        if available_money < 0:
            available_money = 0

    elif action == "save":
        available_money += amount
        counter_spend = 0



    if counter_spend == 5:
        print("You can't save the money.")
        print(days_passed)
        break

    if available_money >= needed_money:
        print(f"You saved the money for {days_passed} days.")
        break