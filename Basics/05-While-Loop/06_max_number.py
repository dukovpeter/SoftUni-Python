import sys

new_input = input()
max_number = -sys.maxsize

while new_input != "Stop":
    number = int(new_input)

    if number > max_number:
        max_number = number

    new_input = input()

print(max_number)



