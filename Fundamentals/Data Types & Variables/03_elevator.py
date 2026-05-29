import math

persons = int(input())
capacity = int(input())
needed_courses = math.ceil(persons / capacity)
print(needed_courses)