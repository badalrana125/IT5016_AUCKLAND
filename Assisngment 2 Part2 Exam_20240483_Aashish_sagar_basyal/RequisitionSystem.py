"""
To Create Requisition System 
Author: Aashish Sagar Basyal
"""

class RequisitionSystem:
    _id_counter = 10000

    def __init__(self):
        self.requests = []
        
    # Collect user information
    def staff_info(self, name, email, date, staff_id):
        user_id = RequisitionSystem._id_counter
        RequisitionSystem._id_counter += 1
        
        last_three = name[-3:]
        id_last_three = str(user_id)[-3:]  #
        reference_number = f"{last_three.upper()}{id_last_three}"
        
        unique_id = RequisitionSystem._id_counter
        
        return {
            "user_id": user_id,
            "name": name,
            "email": email,
            "date": date,
            "reference_number": reference_number,
            "unique_id": unique_id,
            "staff_id": staff_id
        }

#making the list of items and calculate the total amount
    def requisition_details(self, items_with_costs):
        total_amount = sum(cost for item, cost in items_with_costs)
        item_list = [item for item, cost in items_with_costs]
        return total_amount, item_list


    def requisition_approval(self, total_amount):
        return "approved" if total_amount < 150 else "pending"

    def respond_requisition(self, user_id, response):
        for request in self.requests:
            if request["user_id"] == user_id:
                if request["status"] == "pending":
                    request["status"] = response
                break

#To display the requisitions
    def display_requisitions(self):
        if not self.requests:
            print("No requisitions to display.")
            return
 #Displying output       
        for request in self.requests:
            print("\nPrinting Requisitions")
            print(f"Date: {request['date']}")
            print(f"Requisition ID: {request['unique_id']}")
            print(f"Staff ID: {request['staff_id']}")
            print(f"Staff Name: {request['name']}")
            print(f"Total: ${request['total_amount']:.2f}")
            print(f"Status: {request['status']}")
            print(f"Approval Reference Number: {request['reference_number']}")
            print("-" * 40)

#To display requisition statistics
    def requisition_statistic(self):
        total_requests = len(self.requests)
        approved_requests = sum(1 for request in self.requests if request["status"] == "approved")
        pending_requests = sum(1 for request in self.requests if request["status"] == "pending")
        not_approved_requests = sum(1 for request in self.requests if request["status"] == "not approved")
        
        print("\nRequest Statistics:")
        print(f"Total Requests Submitted: {total_requests}")
        print(f"Total Approved Requests: {approved_requests}")
        print(f"Total Pending Requests: {pending_requests}")
        print(f"Total Not Approved Requests: {not_approved_requests}")

    def add_request(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        date = input("Enter the date: ")
        staff_id = input("Enter your staff ID: ")

        items_with_costs = []
        while True:
            item = input("Enter item name (or type 'done' to finish): ").strip().lower()
            if item == 'done':
                break
            cost = float(input(f"Enter the cost for {item}: "))
            items_with_costs.append((item, cost))

        user_info = self.staff_info(name, email, date, staff_id)
        total_amount, item_list = self.requisition_details(items_with_costs)
        status = self.requisition_approval(total_amount)

        request = {
            "user_id": user_info["user_id"],
            "name": user_info["name"],
            "date": user_info["date"],
            "staff_id": user_info["staff_id"],
            "total_amount": total_amount,
            "status": status,
            "reference_number": user_info["reference_number"],
            "unique_id": user_info["unique_id"]
        }

        self.requests.append(request)


if __name__ == "__main__":
    system = RequisitionSystem()
    
    system.add_request() # Add First Request
    system.add_request()  # Adding Second Request
    system.add_request()  # Adding Third Request
    system.add_request()  #Adding  forth Request
    system.add_request()  #Adding fifth Request
    system.display_requisitions()  # Display all requests
    system.respond_requisition(10000, "not approved")  
    system.requisition_statistic()
