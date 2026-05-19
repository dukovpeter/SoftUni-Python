age = int(input())
stage = ""
drink = ""

if age <= 14:
    drink = "toddy"
    print(f"drink {drink}")
elif 14 < age <= 18:
    drink = "coke"
    print(f"drink {drink}")
elif 18 < age <= 21:
    drink = "beer"
    print(f"drink {drink}")
else:
    drink = "whisky"
    print(f"drink {drink}")