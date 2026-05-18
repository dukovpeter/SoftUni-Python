text=input("")
vowel = 0

for char in text:
    if char== "a":
        vowel += 1
    elif char == "e":
        vowel += 2
    elif char == "i":
        vowel += 3
    elif char == "o":
        vowel += 4
    elif char == "u":
        vowel += 5

print(vowel)