while True:

    destination = input("")
    if destination == "End":
        break

    budget = float(input())
    saved_money = 0

    while saved_money < budget:
        save = float(input(""))
        saved_money += save

    print(f"Going to {destination}!")
