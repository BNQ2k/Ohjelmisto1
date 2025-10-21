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

autot = []
for i in range(1, 11):
    reg_tunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    uusi_auto = auto(reg_tunnus, huippunopeus)
    autot.append(uusi_auto)
kilpailu_ohi = False
tunnit_kulunut = 0
matkan_rajapyykki = 10000

print("AUTOKILPAILU ALKAA")
print(f"Tavoitematka: {matkan_rajapyykki} km")
print("-" * 35)

while not kilpailu_ohi:
    tunnit_kulunut += 1
    for a in autot:
        nopeuden_muutos = random.randint(-10, 15)
        a.kiihdyta(nopeuden_muutos)
        a.kulje(1)
        if a.dt >= matkan_rajapyykki:
            kilpailu_ohi = True
            break

print(f"Kilpailu päättyi! Kesto: {tunnit_kulunut} tuntia.")
print(f"Voittaja saavutti vähintään {matkan_rajapyykki} km.")
print("-" * 75)
print(f"{'Rekisteritunnus':<15}{'Huippunopeus (km/h)':<22}{'Viimeinen Nopeus (km/h)':<25}{'Matka (km)':<10}")
print("-" * 75)

for a in autot:
    print(f"{a.reg:<15}{a.ts:<22}{a.cs:<25}{a.dt:<10.2f}")

print("-" * 75)