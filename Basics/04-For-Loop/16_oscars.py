name_actor = input()
points_academy = float(input())
n = int(input())

total_points = points_academy
is_nominated = False

for _ in range(n):
    name_voter = input()
    points_voter = float(input())

    total_points += len(name_voter) * points_voter / 2

    if total_points > 1250.5:
        is_nominated = True
        print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
        break

if not is_nominated:
    needed = 1250.5 - total_points
    print(f"Sorry, {name_actor} you need {needed:.1f} more!")