class Car:
    def __init__(self,color, model, year) -> None:
        self.color = color
        self.model= model
        self.year = year

    def cars(self):
        print(f"The color of the car is: {self.color}, Model is {self.model}, Year is {self.year}")

car1 = Car("Black","Tesla","2004")
car1.cars()