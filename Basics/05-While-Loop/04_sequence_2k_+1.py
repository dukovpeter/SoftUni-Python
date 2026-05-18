n = int(input())
new_number = 0

while True:
    new_number = (new_number * 2) + 1

    if new_number > n:
        break
    print(new_number)