tournaments = int(input())
starting_points_tournament = int(input())
added_points = 0
won_tournaments = 0

for num in range(tournaments):
    reached_stage = input("")

    if reached_stage == "W":
        added_points += 2000
        won_tournaments += 1
    elif reached_stage == "F":
        added_points += 1200
    elif reached_stage == "SF":
        added_points += 720

total_points = starting_points_tournament + added_points
average_points = int( added_points / tournaments )
percent_won_tournament = (won_tournaments / tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent_won_tournament:.2f}%")

