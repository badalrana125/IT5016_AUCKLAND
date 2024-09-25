
def shopping_list():
    print("Welcome to the shopping list Program!")
    shopping_list = []
    total_price = 0
    while True:
        item= input("Enter The Name of the item (or type 'done' to finish): ")
        if item.lower() == 'finish':
            break
        try: 
            price= float(input(f"Enter the price of '{item}': "))
            shopping_list.append((item,price))
            total_price += price 
        except ValueError:
            print("Invalid input... please enter a numeric value for the price.")
          
    return shopping_list, total_price

def main():
    shoopping_list, total_price = shopping_list()
    if not shoopping_list:
        print("No itemes were entered")
    else:
        print("\nShopping List: ")
        for item, price in shoopping_list:
            print(f"{item},${price:2f}")
            print(f"\nTotal price: ${total_price:2f}") 

main() 
    
