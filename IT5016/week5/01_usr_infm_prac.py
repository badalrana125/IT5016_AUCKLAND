"""
Program To collect_user_data
Author= Aashish Sagar Basyal
"""

def collect_user_data(id_counter=5000):
    name= input("Enter your username: ")
    age= int(input("Enter your age: "))
    email= input("Enter your email: ")

    unique_id = id_counter + 1
    user_info= {
      "ID": unique_id,
      "Name": name,
      "Age": age,
      "Email": email
     }
    return user_info
def main(user_info):
    print(f"User Information")
    print(f"Unique ID: {user_info["ID"]}")
    print(f"Name:{user_info["Name"]}")
    print(f"Age:{user_info["Age"]}")
    print(f"Email:{user_info["Age"]}")
user_info = collect_user_data()
main(user_info)
# collect_user_data()

