"""
Proogram to collect staff member information and info
Author: Aashish Sagar Basyal
"""
#using def function
def staff_info(counter_id=10000):
    staff_name= input("Enter your name: ")
    date= input("Enter a date: ")
    staff_id= input("Enter your staff id: ")
    
    requisition_id= counter_id+1
#Displaying data==11
    staff_information={
    "Date": date,
    "ID": staff_id,
    "Name": staff_name,
    "Req_ID": requisition_id
    }
    return staff_information
#using main function to print staff information==19
def main(staff_information):
    print(f"\n Printing Staff Information")
    print(f"Date:{staff_information['Date']}")
    print(f"Staff ID:{staff_information['ID']}")
    print(f"Staff Name:{staff_information['Name']}")
    print(f"Requisition ID:{staff_information['Req_ID']}")
staff_information=staff_info()
main(staff_information)



