water_tank = 255
n = int(input())
total_liters = 0

for l in range(n):
    liters_of_water = int(input())

    if liters_of_water > water_tank:
        print(f"Insufficient capacity!")
    else:
        water_tank -= liters_of_water
        total_liters += liters_of_water

print(total_liters)