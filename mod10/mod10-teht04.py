import random

class Kilpailu:
    def __init__(self, nimi, tunti, km_määrä):
        self.nimi = nimi
        self.tunti = tunti
        self.autot = []
        self.km_määrä = km_määrä
    def luo_autolista(self):
        for i in range(1,11):
            car = Car(i)
            self.autot.append(car)
    def tunti_kuluu(self):
        for car in self.autot:
            car.accelerate()
            car.kulje_tunti()
        self.tunti += 1
    def tulosta_tilanne(self):
        if self.tunti % 10 == 0:
            print(f"Tunti: {self.tunti}")
            for car in self.autot:
                print(f"Auton {car.name} nopeus on {car.speed}km/h ja kuljettu matka on {car.trip}km")
    def kilpailu_ohi(self):
        for car in self.autot:
            if car.trip > self.km_määrä:
                print(f"Kilpailu ohi! Voittaja {car.name}, matka: {car.trip}km")
                return True
        return False


class Car:
    def __init__(self, number):
        self.speed = 40
        self.trip = 0
        self.top_speed = random.randint(150, 200)
        self.name = f"ABC-{number}"
    def accelerate(self):
        self.speed += random.randint(-10, 15)
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.top_speed:
            self.speed = self.top_speed
    def kulje_tunti(self):
        self.trip += self.speed

kisa = Kilpailu("Suuri Romuralli", 0, 8000)
kisa.luo_autolista()

print("Kisa alkaa!")

while True:
    kisa.tunti_kuluu()
    if kisa.tunti % 10 == 0:
        kisa.tulosta_tilanne()
        input("press enter to continue...")
    if kisa.kilpailu_ohi():
        break



