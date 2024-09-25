class RequestSystem:
    #unique ID counter
    request_id_counter = 1

    def __init__(self):
        self.requests = []
        
    def user_info(self, name, age, email):
        self.user_data = {
            'name': name,
            'age': age,
            'email': email
        }
    
    def request_details(self, items_with_costs):
        total = sum(item['cost'] for item in items_with_costs)
        self.requests.append({
            'request_id': RequestSystem.request_id_counter,
            'user': self.user_data,
            'items': items_with_costs,
            'total': total,
            'status': 'pending' if total >= 150 else 'approved'
        })
        RequestSystem.request_id_counter += 1
        return total, items_with_costs

    def request_approval(self):
        last_request = self.requests[-1]
        return last_request['status']


    def respond_request(self, request_id, response):
        for request in self.requests:
            if request['request_id'] == request_id:
                if request['status'] == 'pending':
                    request['status'] = 'approved' if response == 'approved' else 'not approved'
                    break

    def display_request(self):
        for request in self.requests:
            print(f"Request ID: {request['request_id']}")
            print(f"User: {request['user']['name']}, Age: {request['user']['age']}, Email: {request['user']['email']}")
            print(f"Items: {request['items']}")
            print(f"Total: ${request['total']}")
            print(f"Status: {request['status']}")
            print("------------------------")

request_system = RequestSystem()
request_system.user_info("John Doe", 30, "john.doe@example.com")
items = [{'item': 'Laptop', 'cost': 1000}, {'item': 'Mouse', 'cost': 50}]
request_system.request_details(items)
print(request_system.request_approval())
request_system.respond_request(1, 'approved')
request_system.display_request()
request_system.request_statistic()
