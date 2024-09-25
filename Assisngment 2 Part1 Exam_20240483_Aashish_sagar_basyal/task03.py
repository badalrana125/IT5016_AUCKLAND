"""
Program  to make approval decisions
Author: Aashish Sagar Basyal
"""
#using def funstion 
def requisition_approval():
    total_amount=0.00
    counter_id= 10000
#using while
    while True:
        item_name= input("Enter the item name(or type 'finish' to end): ")
        if item_name.lower()== "finish":
            break
        item_price= float(input("Enter the item price(or type'finish' to end): "))
        try:
         total_amount+= item_price
        except ValueError:
         print("\nPlease Enter a valid Number")
    print(f"The total price of items is:${total_amount:.2f}")
#if and else for approval or pending
    if total_amount < 500:
        Status = "Approved"
        requisition_id= counter_id+1
        print(f"Status:{Status}")
        print(f"Approval Reference Nmuber:{requisition_id}")
    else:
        Status ="Pending"
        print(f"Status:{Status}")
#closing the def funtion to get output
requisition_approval()



