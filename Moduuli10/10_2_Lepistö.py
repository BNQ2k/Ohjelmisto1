class hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros
    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Going Up. Floor: {self.nykyinen_kerros}")
    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Going Down. Floor: {self.nykyinen_kerros}")
    def siirry_kerrokseen(self, missio):
        while self.nykyinen_kerros < missio:
            self.kerros_ylos()
        while self.nykyinen_kerros > missio:
            self.kerros_alas()

class talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.hissit = []
        for i in range(hissien_maara):
            uusi_hissi = hissi(alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)
    def aja_hissia(self, hissi_numero, kerros):
        self.hissit[hissi_numero].siirry_kerrokseen(kerros)

talo1 = talo(1, 10, 2)
talo1.aja_hissia(0, 5)
talo1.aja_hissia(1, 7)
talo1.aja_hissia(0, 1)
