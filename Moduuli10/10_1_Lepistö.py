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
h = hissi(1, 70)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)