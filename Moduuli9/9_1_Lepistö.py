class auto:
    def __init__(self, reg, ts):
        self.reg = reg
        self.ts = ts
        self.cs = 0
        self.dt = 0

pösö = auto("ABC-123", 142)
print(pösö)
print("Auton ominaisuudet: ")
print(f"Rekisteritunnus: {pösö.reg}")
print(f"Huippunopeus: {pösö.ts} km/h")
print(f"Nopeus nyt: {pösö.cs} km/h")
print(f"Matka: {pösö.dt} km")