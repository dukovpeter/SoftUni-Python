n = int(input())
salary = int(input())

for num in range(n):
    tab = input("")

    if tab == "Facebook":
        salary -= 150
    elif tab == "Instagram":
        salary -= 100
    elif tab == "Reddit":
        salary -= 50
    else:
        fee = 0

if salary <= 0:
    print(f"You have lost your salary.")
    exit()
else:
    print(salary)
    exit()

