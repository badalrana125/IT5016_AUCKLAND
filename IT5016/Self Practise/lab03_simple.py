class RequestSystem:
    _id_counter = 1000
    print("Displaying All Requests: ")

    def __init__(self):
        self.requests = []

    def add_request(self):
        name = input("Enter your name: ")
        items_with_costs = []
        while True:
            item = input("Enter item name (or type 'done' to finish): ").strip().lower()
            if item == 'done':
                break
            cost = float(input(f"Enter the cost for {item}: "))
            items_with_costs.append(cost)

        user_id = RequestSystem._id_counter
        last_three_letters = name[-3:] if len(name) >= 3 else name
        user_id = f"{RequestSystem._id_counter}{last_three_letters.lower()}"
        RequestSystem._id_counter += 2
        total_amount = sum(items_with_costs)
        status = "approved" if total_amount < 150 else "pending"

        self.requests.append({"user_id": user_id, "name": name, "total_amount": total_amount, "status": status})

    def display_requests(self):
        for request in self.requests:
            print(f"User ID: {request['user_id']}, Name: {request['name']}, Total Amount: ${request['total_amount']:.2f}, Status: {request['status']}")
            print("-" * 40)

    def respond_request(self, user_id, response):
        for request in self.requests:
            if request["user_id"] == user_id and request["status"] == "pending":
                request["status"] = response
                break

    def request_statistics(self):
        total_requests = len(self.requests)
        approved = sum(1 for r in self.requests if r["status"] == "approved")
        pending = sum(1 for r in self.requests if r["status"] == "pending")
        print(f"Total Requests: {total_requests}, Approved: {approved}, Pending: {pending}")

if __name__ == "__main__":
    system = RequestSystem()

    system.add_request()
    system.add_request()
    system.add_request()
    system.display_requests()
    system.respond_request(1000, "not approved")
    system.request_statistics()
