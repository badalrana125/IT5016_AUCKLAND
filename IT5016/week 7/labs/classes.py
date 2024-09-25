class Person():
    def __init__(self, name, gender) -> None:
        self.name = name
        self.age = 25
        self.gender= gender

    def speaks(self):
            quote= input(f"What does the {self.name} say?")
            quote02 = input(f"I'm {self.age} years age.")
            print(quote, quote02)


person1 = Person("Rashid", "male")
person2 = Person("kanchan","Female")

person1.speaks()