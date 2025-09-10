def funktio(lista):
    uusilista = []
    for luku in lista:
        if luku % 2 == 0:
            uusilista.append(luku)
    return uusilista
lista = [1, 2, 3, 4, 5, 6]
print(funktio(lista))
print(lista)