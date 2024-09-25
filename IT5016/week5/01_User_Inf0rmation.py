"""
To get User Information
Author: Aashish Sagar Basyal
"""
def collect_user_id(id_counter=5000):
    name = input("Enter Your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email address: ")
    unique_id = id_counter + 1
    
    # Collect user information
    user_info = {
        "ID": unique_id,
        "Name": name,
        "Age": age,
        "EMAIL": email
    }
    
    return user_info

def main(user_info):
    print(f"\n User Information")
    print(f"Unique ID: {user_info['ID']}")
    print(f"Name: {user_info['Name']}")
    print(f"Age: {user_info['Age']}")
    print(f"Email: {user_info['EMAIL']}")

# Collect user information
user_info = collect_user_id()

main(user_info)