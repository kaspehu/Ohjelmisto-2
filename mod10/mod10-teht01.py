class Hissi:
    def __init__(self, alin_kerros, nykyinen_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.nykyinen_kerros = nykyinen_kerros
        self.ylin_kerros = ylin_kerros
    def hissi_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
    def hissi_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
    def siirry_kerrokseen(self, kerrokseen):
        print(f"Siirrytään kerrokseen {kerrokseen}.")
        if kerrokseen < self.alin_kerros or kerrokseen > self.ylin_kerros:
            print("Virheellinen kerros!")
        while self.nykyinen_kerros < kerrokseen:
            self.hissi_ylos()
            print(f"Olet kerroksessa {self.nykyinen_kerros}.")

        while self.nykyinen_kerros > kerrokseen:
            self.hissi_alas()
            print(f"Olet kerroksessa {self.nykyinen_kerros}.")





# määritetään alimmaksi kerrokseksi 0, tämänhetkiseksi kerrokseksi 0, ja ylimmäksi 10
hissi1 = Hissi(0, 0, 10)

hissi1.siirry_kerrokseen(5)
hissi1.siirry_kerrokseen(0)