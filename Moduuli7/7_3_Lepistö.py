lentoasematiedot = {}
while True:

    print("1 = Syötä uusi lentoasema.")
    print("2 = Hae lentoaseman tiedot.")
    print("3 = Lopeta.")
    valinta123 = input("Mitä haluat tehdä? 1, 2 vai 3?: ")

    if valinta123 == "1":
        koodi = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi:")
        lentoasematiedot[koodi] = nimi
        print("Tallennettu")


    elif valinta123 == "2":

        koodi = input("Anna ICAO-koodi: ")
        if koodi in lentoasematiedot:
            print("Lentoasema: ", lentoasematiedot[koodi])
        else:
            print("Lentoasemaa ei löydy.")


    elif valinta123 == "3":
        print("Näkemiin!")
        break