number = int(input())
bonus_gain = 0

if number <= 100:
    bonus_gain = 5
elif 100 < number <= 1000:
    bonus_gain = 0.2 * number
elif number > 1000:
    bonus_gain = 0.1 * number

if number % 2 == 0:
    bonus_gain = bonus_gain + 1
elif number % 10 == 5:
    bonus_gain = bonus_gain + 2

print(bonus_gain)
print(bonus_gain + number)