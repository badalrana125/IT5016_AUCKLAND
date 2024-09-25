def function1(n1,n2,n3):
    sum= n1 + n2 + n3
    minimum= min(n1,n2,n3)
    total= sum - minimum
    return total

n1 = int(input("number 1: "))
n2 = int(input("number 2: "))
n3 = int(input("numer 3: "))
print(function1(n1,n2,n3))
