def celsius_to_f(celsius):
    fahrenheiet: celsius *9 / 5+ 32 # type: ignore
    return fahrenheiet

celsius = float(input("Enter the Celsius: "))
print(celsius_to_f(celsius))


