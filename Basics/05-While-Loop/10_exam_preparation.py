fail_limit = int(input())

total_ratings = 0
num_ratings = 0
num_fails = 0
last_name = ""

while True:
    task_name = input()

    if task_name == "Enough":
        average_score = total_ratings / num_ratings

        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {num_ratings}")
        print(f"Last problem: {last_name}")
        break

    rating = int(input())

    total_ratings += rating
    num_ratings += 1
    last_name = task_name

    if rating <= 4:
        num_fails += 1

    if num_fails == fail_limit:
        print(f"You need a break, {num_fails} poor grades.")
        break