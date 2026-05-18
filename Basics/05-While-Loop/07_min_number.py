import sys

new_input = input()
min_number = sys.maxsize

while new_input != "Stop":
    number = int(new_input)

    if number < min_number:
        min_number = number

    new_input = input()

print(min_number)



