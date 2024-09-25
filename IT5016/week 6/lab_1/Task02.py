class Rectangle():
    def __init__(self,width,height) -> None:
        self.weidth = width
        self.height = height

    def area(self):
        return self.weidth * self.height
    
    def perimeter(self):
        return 2*(self.weidth + self.height)

rect= Rectangle(4,5)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}") 