
item_1 = float (input("Input the price for item "))
item_2 = float (input("Input the price for item "))
item_3 = float (input("Input the price for item "))
subtotal = item_1 + item_2 + item_3

salesGST= subtotal * 0.15
total = subtotal+ salesGST
print("Your purchase total is $", total, sep="")



