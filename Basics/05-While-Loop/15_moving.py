width_space = int(input())
length_space = int(input())
height_space = int(input())

total_free_space = width_space * length_space * height_space

while True:
    command = input()
    if command == 'Done':
        print(f"{total_free_space} Cubic meters left.")
        break

    boxes = int(command)
    total_free_space -= boxes

    if total_free_space <= 0:
        print(f"No more free space! You need {abs(total_free_space)} Cubic meters more.")
        break