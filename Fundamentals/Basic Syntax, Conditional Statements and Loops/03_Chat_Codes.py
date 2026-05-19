messages = int(input())

for num in range(messages):
    new_number = int(input())

    if new_number == 88:
        print("Hello")
    elif new_number == 86:
        print("How are you?")
    elif new_number < 88:
        print("GREAT!")
    elif new_number == 87:
        print("GREAT!")
    else:
        print("Bye.")