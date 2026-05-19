coffees = 0
command = input()

while command != "END":

    if command in ["dog", "cat", "movie", "coding",
                   "DOG", "CAT", "MOVIE", "CODING"]:
        if command.islower():
            coffees += 1

        elif command.isupper():
            coffees += 2
    command = input()


if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)

