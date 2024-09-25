"""
Program to calculate the total price of the requisition items
Author: Aashish Sagar Basyal
"""
#using def function
def requisitions_total():
    total_amount=0.00
#using while,if, break, try,except
    while True:
        item_name= input("Enter the item name(or type 'finish' to end): ")
        if item_name.lower()== "finish":
            break
        item_price= float(input("Enter the item price(or type'finish' to end): "))
        try:
         total_amount+= item_price
        except ValueError:
         print("Please Enter a valid Number")
    print(f"The total price of items:${total_amount:.2f}")
requisitions_total()
