lista = []
while True:

    nimi = input("Syötä nimi: ")
    if nimi == "":
        break




    if nimi in lista:
        print("Nimi on jo listassa.")
    else:
        print("Uusi nimi")
        lista.append(nimi)


print("\nSyötetyt nimet: ")
for i in lista:

    print(i)