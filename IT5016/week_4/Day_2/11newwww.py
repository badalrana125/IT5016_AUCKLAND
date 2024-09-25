def shopping_list():
    items = []
    total = 0

    while True:
        item = input("Enter item name (or 'done' to finish): ")
        if item.lower() == 'done':
            break

        try:
            price = float(input("Enter item price: "))
            items.append((item, price))
            total += price
        except ValueError:
            print("Please enter a valid number for the price.")

    return items, total

def main():
    items, total = shopping_list()
    
    if items:
        print("\nYour Shopping List:")
        for item, price in items:
            print(f"{item}: ${price:.2f}")
        print(f"\nTotal: ${total:.2f}")
    else:
        print("No items were added.")

main()
