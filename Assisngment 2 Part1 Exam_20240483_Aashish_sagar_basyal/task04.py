def staff_info(counter_id=10000):
    staff_name = input("Enter your name: ")
    date = input("Enter a date: ")
    staff_id = input("Enter your staff id: ")
    requisition_id = counter_id + 1

    # Displaying data
    staff_information = {
        "Date": date,
        "ID": staff_id,
        "Name": staff_name,
        "Req_ID": requisition_id
    }
    return staff_information

def requisition_approval(counter_id=10000):
    total_amount = 0.00
    
    while True:
        item_name = input("Enter the item name (or type 'finish' to end): ")
        if item_name.lower() == "finish":
            break
        
        try:
            item_price = float(input("Enter the item price: "))
            total_amount += item_price
        except ValueError:
            print("\nPlease enter a valid number.")
    
    print(f"The total price of items is: ${total_amount:.2f}")
    
    # Approval or pending
    if total_amount < 500:
        status = "Approved"
        requisition_id = counter_id + 1
        print(f"Status: {status}")
        print(f"Approval Reference Number: {requisition_id}")
    else:
        status = "Pending"
        requisition_id = None
    
    return total_amount, status, requisition_id

def create_detailed_report(total_amount, staff_information, status, requisition_id):
    print("\nPrinting Requisitions:")
    print(f"Date: {staff_information['Date']}")
    print(f"Requisition ID: {staff_information['Req_ID']}")
    print(f"Staff ID: {staff_information['ID']}")
    print(f"Staff Name: {staff_information['Name']}")
    print(f"Total: ${total_amount:.2f}")
    print(f"Status: {status}")
    # if requisition_id:
    print(f"Approval Reference Number: {requisition_id}")
#Using main function to display data
def main():
    staff_information = staff_info()
    total_amount, status, requisition_id = requisition_approval()
    create_detailed_report(total_amount, staff_information, status, requisition_id)

main()
