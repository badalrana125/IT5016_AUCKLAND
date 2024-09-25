class Car:
    def __init__(self,color,model) -> None:
        self.color= color
        self.model= model
    def drive(self):
        print(f"The {self.color} {self.model} is driving.")
    
    def stop(self):
        print(f"The {self.color} {self.model} is stopped.")
    
car1= Car("Red", "Toyata")
car2= Car("Blue", "Honda")
car1.drive()
car2.stop()