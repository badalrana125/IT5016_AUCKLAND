def what_to_wear (temperature):
    if temperature>25:
        print("wear shorts.")
    else:
            print("Not hot today!")
            print("Wear long pants.")
    print("Enjoy yourrself")

def main():
    what_to_wear(20)
    print()
    what_to_wear(30)

main()