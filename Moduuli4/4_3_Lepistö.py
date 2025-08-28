luku = input("Anna luku: ")

numerolista = []
while luku != "":
    luku = int(luku)
    numerolista.sort()
    numerolista.append(luku)
    print(numerolista)
    luku = input("Anna luku: ")

print(f"Isoin numero on {numerolista [-1]}.")
print(f"Isoin numero on {numerolista [0]}.")