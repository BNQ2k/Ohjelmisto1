def summa(lista):
    return sum(lista)

def main():
    luvut = []
    print("Syötä kokonaislukuja yksi kerrallaan. Enter ilman lukua lopettaa ohjelman.")
    while True:
        syote = input("Anna luku: ")
        if syote == "":
           break
        try:
            luku = int(syote)
            luvut.append(luku)
        except ValueError:
            print("Virheellinen syöte. Anna kokonaisluku.")
    yhteensa = summa(luvut)
    print(f"Listan summa on {yhteensa}.")



main()