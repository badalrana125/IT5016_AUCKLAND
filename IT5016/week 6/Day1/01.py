class Person():
    def __init__(self,name, age) -> None:
        self.name= name
        self.age= age

person1= Person("James", 30)
person2= Person("Jessica",25)

print(person1.name)
print(person1.age)
print(person2.age)