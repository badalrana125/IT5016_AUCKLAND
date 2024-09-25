def calculate_total_amount():
    total_amount = 0.0
    
    while True:
        item_name= input("Enter the name of the item (or type 'finish' to end): ")
        
        if item_name.lower() == "finish":
            break
        
        price = input("Enter the price of the item (or type 'finish' to end): ")
        try:
            total_amount += float(price)
        except ValueError:
            print("Please enter a valid price.")
    
    print(f"The total amount is: ${total_amount:.2f}")

#calculate the total amount
calculate_total_amount()
