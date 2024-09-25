def calculate_total_amount():
    total_amount= 0.00
    while True: 
        name = input("Enter item name(or type 'finish' to end: )")
        if name.lower() == "finish":
            break
        price= int(input("Enter item price(or type 'finish' to end: )"))
        
        try:
           total_amount += float(price)
        except ValueError:
            print("please enter the valid price")
    print(f"The total amount of is:${total_amount: .2f}")
calculate_total_amount()