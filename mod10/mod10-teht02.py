

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
        if kerrokseen < self.alin_kerros or kerrokseen > self.ylin_kerros:
            print("Virheellinen kerros!")
            return
        while self.nykyinen_kerros < kerrokseen:
            self.hissi_ylos()
            print(f"Olet kerroksessa {self.nykyinen_kerros}.")

        while self.nykyinen_kerros > kerrokseen:
            self.hissi_alas()
            print(f"Olet kerroksessa {self.nykyinen_kerros}.")



class Talo:
    def __init__(self, alin_kerros, nimi, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.nimi = nimi
        self.hissit = []
        self.ylin_kerros = ylin_kerros
    def lisää_hissit(self, hissi):
            self.hissit.append(hissi)
    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if hissin_numero < 0 or hissin_numero >= len(self.hissit):
            print("Virheellinen hissinumero!")
            return
        print(f"Hissi {hissin_numero + 1} talossa {self.nimi} liikkuu kerrokseen: {kohde_kerros} ")
        self.hissit[hissin_numero].siirry_kerrokseen(kohde_kerros)



hissi1 = Hissi(0, 5, 10)
hissi2 = Hissi(0, 2, 10)
hissi3 = Hissi(0, 3, 10)
hissi4 = Hissi(0, 4, 15)

talo1 = Talo(0, "Talo1", 10)
talo2 = Talo(0, "Talo2", 15)

talo1.lisää_hissit(hissi1)
talo1.lisää_hissit(hissi2)

talo2.lisää_hissit(hissi3)
talo2.lisää_hissit(hissi4)

talo1.aja_hissiä(0, 10)
talo2.aja_hissiä(1, 15)