class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0
    def kiihdyta(self, muutos):
        uusi_nopeus = self.tamanhetkinen_nopeus + muutos

        if uusi_nopeus <= 0:
            self.tamanhetkinen_nopeus = 0
        elif uusi_nopeus >= self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        else:
            self.tamanhetkinen_nopeus = uusi_nopeus
    def kulje(self, tunnit):
        kuljettu = self.tamanhetkinen_nopeus * tunnit
        self.kuljettu_matka += kuljettu
class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti_kWh):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti_kWh = akkukapasiteetti_kWh
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko_l):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko_l = bensatankin_koko_l
if __name__ == "__main__":
    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)
    sahkoauto.kiihdyta(100)
    polttomoottoriauto.kiihdyta(95)
    ajoaika = 3
    sahkoauto.kulje(ajoaika)
    polttomoottoriauto.kulje(ajoaika)
    print("Autojen matkamittarilukemat")
    print(f"Sähköauto ({sahkoauto.rekisteritunnus}, {sahkoauto.akkukapasiteetti_kWh} kWh):")
    print(f"  Kuljettu matka: {sahkoauto.kuljettu_matka:.2f} km\n")
    print(f"Polttomoottoriauto ({polttomoottoriauto.rekisteritunnus}, {polttomoottoriauto.bensatankin_koko_l} l):")
    print(f"  Kuljettu matka: {polttomoottoriauto.kuljettu_matka:.2f} km")