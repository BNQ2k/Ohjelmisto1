class hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1

    def siirry_kerrokseen(self, missio):
        while self.nykyinen_kerros < missio:
            self.kerros_ylos()
        while self.nykyinen_kerros > missio:
            self.kerros_alas()

class talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.alin_kerros = alin_kerros
        self.hissit = []
        for i in range(hissien_maara):
            uusi_hissi = hissi(alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)
    def aja_hissia(self, hissi_numero, kerros):
        if 0 <= hissi_numero < len(self.hissit):
            self.hissit[hissi_numero].siirry_kerrokseen(kerros)

    def palohalytys(self):
        for hissi_olio in self.hissit:
            hissi_olio.siirry_kerrokseen(self.alin_kerros)
talo1 = talo(1, 10, 2)
talo1.aja_hissia(0, 5)
talo1.aja_hissia(1, 7)
talo1.aja_hissia(0, 1)
talo1.palohalytys()

print(f"Hissi 1 kerroksessa: {talo1.hissit[0].nykyinen_kerros}")
print(f"Hissi 2 kerroksessa: {talo1.hissit[1].nykyinen_kerros}")