import sys

n = int(input())

max_num = -sys.maxsize
total = 0

for _ in range(n):
    num = int(input())
    total += num

    if num > max_num:
        max_num = num

rest = total - max_num

if max_num == rest:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(max_num - rest)}")