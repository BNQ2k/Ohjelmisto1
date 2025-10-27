class julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
class kirja(julkaisu):
    def __init__(self, kirjannimi, kirjailija, sivuja):
        super().__init__(kirjannimi)
        self.kirjailija = kirjailija
        self.sivuja = sivuja
    def tulosta_tiedot(self):
        print("--- Kirja ---")
        print(f"Nimi: {self.nimi}")
        print(f"Kirjailija: {self.kirjailija}")
        print(f"Sivumäärä: {self.sivuja}")


class lehti(julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja
    def tulosta_tiedot(self):
        print("--- Lehti ---")
        print(f"Nimi: {self.nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja}")
if __name__ == "__main__":
    akuankka = lehti("Aku Ankka", "Aki Hyyppä")
    hytti_nro6 = kirja("Hytti n:o 6", "Rosa Liksom", 200)

    print("--- JULKAISUTIEDOT ---")

    # Kutsutaan metodeja
    akuankka.tulosta_tiedot()

    print("==========================")

    hytti_nro6.tulosta_tiedot()

    print("==========================")