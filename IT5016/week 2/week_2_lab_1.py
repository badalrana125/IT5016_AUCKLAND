"""
calculating the person's age
Author: Aashish
"""
#question_1
name= input("What is Your name: ")
date_birth= int(input("What is your birth year: "))
current_year=int(input("Current Year: "))
current_age= current_year - date_birth
print("Hey", name, "you are now", current_age, ". WoW!!",)


#question 2

a=42
b=3.14
c="Hello, World!"
d=[1,2,3]
e= (1,2,3)
f={"name":"John","age":30}

#a
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

#b
b=3.14
string_value= str(b)
print(string_value)
print(type(string_value))



# colour = input("what is your favourite colour: ")