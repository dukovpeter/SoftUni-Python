num_groups = int(input())

mount1 = 0
mount2 = 0
mount3 = 0
mount4 = 0
mount5 = 0

total_people = 0

for i in range(num_groups):
    num_people_groups = int(input())
    total_people += num_people_groups

    if num_people_groups <= 5:
        mount1 += num_people_groups
    elif 6 <= num_people_groups <= 12:
        mount2 += num_people_groups
    elif 13 <= num_people_groups <= 25:
        mount3 += num_people_groups
    elif 26 <= num_people_groups <= 40:
        mount4 += num_people_groups
    else:
        mount5 += num_people_groups

mount1_percent = (mount1/total_people) * 100
mount2_percent = (mount2/total_people) * 100
mount3_percent = (mount3/total_people) * 100
mount4_percent = (mount4/total_people) * 100
mount5_percent = (mount5/total_people) * 100

print(f"{mount1_percent:.2f}%")
print(f"{mount2_percent:.2f}%")
print(f"{mount3_percent:.2f}%")
print(f"{mount4_percent:.2f}%")
print(f"{mount5_percent:.2f}%")
