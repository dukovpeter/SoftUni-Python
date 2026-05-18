name_student = input("")
grades_sum = 1
grades_total = 0
max_tries = 0

while True:
    new_grade = float(input())
    if new_grade < 4.00:
        max_tries += 1
        if max_tries > 1:
            print(f"{name_student} has been excluded at {grades_sum} grade")
            break
        continue

    grades_total += new_grade

    if grades_sum == 12:
        grades_avg = grades_total / 12
        print(f"{name_student} graduated. Average grade: {grades_avg:.2f}")
        break
    grades_sum += 1