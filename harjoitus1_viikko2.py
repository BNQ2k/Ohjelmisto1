kokonaisluku = int(input("Anna kokonaisluku, 0 lopettaa ohjelman: "))
kertoja = 1
while True:
    kertoja = kertoja + 1
    if kokonaisluku == 0:
        print("Lopetetaan ohjelma.")
        break
    kokonaisluku = kokonaisluku * kertoja
    print(f"Luku kerrottuna {kertoja} on {kokonaisluku}.")
    kokonaisluku = int(input("Anna kokonaisluku, 0 lopettaa ohjelman: "))

