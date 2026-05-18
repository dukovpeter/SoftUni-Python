import math

name_movie = input("")
duration_movie = int(input())
duration_rest = int(input())

time_lunch = duration_rest * 1/8
time_relax = duration_rest * 1/4
time_free = duration_rest - time_lunch - time_relax
time_needed = math.ceil(duration_movie - time_free)
time_left = math.ceil(time_free - duration_movie)

if time_free >= duration_movie:
    print(f"You have enough time to watch {name_movie} and left with {time_left} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_movie}, you need {time_needed} more minutes.")