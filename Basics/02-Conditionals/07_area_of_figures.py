figure = input()

if figure == 'square':
    a = float(input())
    area = a * a

elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b

elif figure == 'circle':
    r = float(input())
    area = 3.14159265359 * r * r

elif figure == 'triangle':
    a = float(input())
    b = float(input())
    area = a * b / 2

print(f"{area:.3f}")