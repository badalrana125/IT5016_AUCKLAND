class Vehicle:
    def __init__(self) -> None:
        pass

    def start(self):
        print(" Vehicle started.")
    
    def stop(self):
        print("vehical stopped")

class Car(Vehicle):
    def honk(self):
        print("Honk Honk")

my_car= Car()
my_car.start()
my_car.honk()
my_car.stop()