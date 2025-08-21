import random

uno = random.randint(0, 9)
dos = random.randint(0, 9)
tres = random.randint(0, 9)
kolmenumeroinen = str(uno) + str(dos) + str(tres)

four = random.randint(1, 6)
five = random.randint(1, 6)
six = random.randint(1, 6)
seven = random.randint(1, 6)

nelinumeroinen = str(four) + str(five) + str(six) + str(seven)

print("Kolmenumeroinen lukon koodi 0-9: " + kolmenumeroinen)
print("Nelinumeroinen lukon koodi 1-6: " + nelinumeroinen)