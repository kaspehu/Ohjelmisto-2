import random

class Car:
    def __init__(self, number):
        self.speed = 80
        self.trip = 0
        self.top_speed = random.randint(100, 200)
        self.name = f"ABC-{number}"
    def accelerate(self):
        self.speed += random.randint(-10, 15)
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.top_speed:
            self.speed = self.top_speed
    def trip_length(self):
        self.trip += self.speed


cars = []
for i in range(1, 11):
    car = Car(i)
    cars.append(car)

winner = None # luodaan voittaja kisan päättäväksi tekijäksi
round = 0
while not winner:
    round += 1 #jokainen kierros ilmaisee "tuntia", sillä arvotun nykyisen nopeuden (km/h) arvo lisätään edelliseen
                # nopeuteen, josta tulee kierroksittain kokonaismatka
    print(f"Round {round}!")
    for car in cars:
        car.accelerate()
        car.trip_length()
        print(f"Car {car.name} current speed is {car.speed}km/h and driven distance {car.trip}km")
        if car.trip >= 10000: # kisa päättyy kun jokin autoista ylittää 10000km
            winner = car
            input("Press enter to continue...")
            break

# printataan voittajan statistiikat
print(f"\nThe winner was {winner.name} with a top speed of {winner.top_speed}km/h and total driven distance {winner.trip}km\n")
input("Press enter to continue...")
#ja lopuksi kaikkien autojen statistiikat
print("\nStatistics for all cars:")
for car in cars:
    print(f"Car {car.name}'s top speed is {car.top_speed}km/h and total driven distance {car.trip}km")


