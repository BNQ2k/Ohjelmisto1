import random
luku = random.randint(1, 10)

while True:
    try:
        arvaus = int(input("Arvaa luku (1-10): "))

        if arvaus < 1 or arvaus > 10:
            print("Anna luku väliltä 1-10.")
            continue

        if arvaus < luku:
            print("Liian pieni arvaus.")
        elif arvaus > luku:
            print("Liian suuri arvaus.")
        else:
            print("Oikein!")
            break
    except ValueError:
        print("Syötä vain kokonaisluku.")
