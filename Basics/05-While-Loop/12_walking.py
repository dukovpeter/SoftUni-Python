goal_steps = 10000
steps_total = 0

while steps_total < goal_steps:
    command = input()

    if command == "Going home":
        steps = int(input())
        steps_total += steps
        break

    steps = int(command)
    steps_total += steps

diff = abs(steps_total - goal_steps)

if steps_total >= goal_steps:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
