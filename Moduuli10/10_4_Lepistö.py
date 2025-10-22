import random
class auto:
    def __init__(self, reg, ts):
        self.reg = reg
        self.ts = ts
        self.cs = 0
        self.dt = 0

    def kiihdyta(self, muutos):
        uusi_nopeus = self.cs + muutos
        if uusi_nopeus <= 0:
            self.cs = 0
        elif uusi_nopeus >= self.ts:
            self.cs = self.ts
        else:
            self.cs = uusi_nopeus
    def kulje(self, tunnit):
        kuljettu = self.cs * tunnit
        self.dt += kuljettu
class Kilpailu:
    def __init__(self, nimi, pituus_km, autolista):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autolista = autolista
        self.tunnit_kulunut = 0
    def tunti_kuluu(self):
        self.tunnit_kulunut += 1
        for a in self.autolista:
            nopeuden_muutos = random.randint(-10, 15)
            a.kiihdyta(nopeuden_muutos)
            a.kulje(1)

    def tulosta_tilanne(self):
        print(f"\nTILANNE KILPAILUSSA: {self.nimi} - {self.tunnit_kulunut} tuntia")
        print(f"{'Rekisteri':<12}{'Huippu (km/h)':>15}{'Nopeus (km/h)':>20}{'Matka (km)':>25}{'Maaliin (km)':>10}")
        for a in self.autolista:
            jaljella = self.pituus_km - a.dt
            print(f"{a.reg:<12}{a.ts:>15}{a.cs:>20}{a.dt:>25.2f}{max(0, jaljella):>10.2f}")
    def kilpailu_ohi(self):
        for a in self.autolista:
            if a.dt >= self.pituus_km:
                return True
        return False

autot = []
for i in range(1, 11):
    reg_tunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    uusi_auto = auto(reg_tunnus, huippunopeus)
    autot.append(uusi_auto)

romuralli = Kilpailu("Suuri romuralli", 8000, autot)
print(f"Kilpailu alkaa: {romuralli.nimi} ({romuralli.pituus_km} km)")
while not romuralli.kilpailu_ohi():
    romuralli.tunti_kuluu()
    if romuralli.tunnit_kulunut % 10 == 0:
        romuralli.tulosta_tilanne()
print("\n!!! KILPAILU PÄÄTTYNYT !!!")
romuralli.tulosta_tilanne()