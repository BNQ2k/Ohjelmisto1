class auto:
    def __init__(self, reg, ts):
        self.reg = reg
        self.ts = ts
        self.cs = 0
        self.dt = 0
    def kiihdyta(self, muutos):
        if self.cs + muutos <= 0:
            self.cs = 0
        elif self.cs + muutos >= self.ts:
            self.cs = self.ts
        else:
            self.cs += muutos
    def kulje(self, tunnit):
        kuljettu = self.cs * tunnit
        self.dt += kuljettu


pösö = auto("ABC-123", 142)
print(pösö)
print("AUTON OMINAISUUDET: ")
print("---------------------")
print(f"Rekisteritunnus: {pösö.reg}")
print(f"Huippunopeus: {pösö.ts} km/h")

pösö.kiihdyta(30)
pösö.kiihdyta(50)
pösö.kiihdyta(70)
print(f"Nopeus nyt: {pösö.cs} km/h")
pösö.kiihdyta(-200)
print(f"Nopeus nyt: {pösö.cs} km/h")

pösö.kiihdyta(60)
pösö.kulje(1.5)
print("Nopeus matkustaessa 60 km/h")
print(f"Matka nyt: {pösö.dt} km")
