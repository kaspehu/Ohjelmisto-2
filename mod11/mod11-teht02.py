import random


class Car:
    def __init__(self, name, top_speed):
        self.speed = 80 # lähtönopeus 80km
        self.trip = 0
        self.top_speed = top_speed
        self.name = name
    def accelerate(self):
        self.speed += random.randint(20, 40) # lisätään nopeutta arpomalla 20-40km/h
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.top_speed:
            self.speed = self.top_speed
    def kulje_tunti(self):
        self.trip += self.speed



class Sähköauto(Car):
    def __init__(self, name, top_speed, akku="52.5kWh"):
        super().__init__(name, top_speed)
        self.akku = akku
        self.top_speed = 180


class Polttomoottoriauto(Car):
    def __init__(self, name, top_speed, tankki="32.3l"):
        super().__init__(name, top_speed)
        self.tankki = tankki
        self.top_speed = 165


cars = []
cars.append(Sähköauto("ABC-15", 180))
cars.append(Polttomoottoriauto("ACD-123", 165))

kierros = 0 # 1 kierros = 1 tunti
print("Kolmen tunnin testi alkaa!")
while kierros < 3:
    kierros += 1
    for car in cars:
        car.accelerate()
        car.kulje_tunti()
        #print(f"{car.speed}, {car.trip}") # poista risuaidat, jos haluat testata
    #input("testiksi")
input("Paina enter paljastaaksesi tulokset: ")
for car in cars:
    if isinstance(car, Sähköauto):
        print(f"Auton {car.name} ({car.akku}) loppunopeus oli {car.speed}km/h ja kuljettu matka {car.trip}km")
    elif isinstance(car, Polttomoottoriauto):
        print(f"Auton {car.name} ({car.tankki}) loppunopeus oli {car.speed}km/h ja kuljettu matka {car.trip}km")


