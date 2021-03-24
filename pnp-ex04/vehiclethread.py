import threading, time

class Vehicle(threading.Thread):
    def __init__(self,type): 
        super().__init__()
        self.type = type
        self.fuel = 10
        if type == "truck":
            self.consumption = .4
            self.speed = 1.5
        else:
            self.consumption = .2
            self.speed = 1

    def run(self):
        while True:
            time.sleep(self.speed)
            if self.fuel<=0:
                print(f"Refilling {self.type} tank...")
                time.sleep(4)
                self.fuel=10
            else:
                print(f"{self.type} is running ({self.fuel:.2f})")
                self.fuel-=self.consumption

car     = Vehicle("truck")
truck   = Vehicle("car")

car.start()
truck.start()
