lista = []

while True:
    mjono = input("Syötä luku, (tyhjä lopettaa)")
    if mjono == "":
        break
    luku = int(mjono)
    lista.append(luku)

lista.sort(reverse=True)
print("Viisi suurinta lukua ovat:")
for luku in lista[:5]:
    print(luku)