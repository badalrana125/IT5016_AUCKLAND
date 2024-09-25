class Person:
    def __init__(self,name,age) -> None:
        self.name = name 
        self.age = age

    def great(self):
        print((f"Hello, my name is {self.name} and I am {self.age} years old."))

person1 = Person("Aashish", 10)
person1.great()