def parittomat(lista):
    parilliset = []
    for luku in lista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

def main():
    alkuperainen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu = parittomat(alkuperainen)
    print("Alkuperäinen lista:", alkuperainen)
    print("Parilliset luvut: ", karsittu)

main()