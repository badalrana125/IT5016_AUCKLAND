"""
Get Information
Author = Aashish
"""
def collect_user_id(id_counter=5000):
    name = input("Enter Your name : ")
    age = int(input("Enter your age: "))
    email = input("Enter your email address: ")
    unique_id = id_counter + 1
   # collect user information
    user_info={
       "ID": unique_id,
       "Name": name,
       "Age": age,
       "EMAIL": email
        }  
    
    return user_info

def main(user_info):
    print("User Information")
    print(f"Unique ID:{user_info['id']}")
    print(f"Name:{user_info['Name']}")
    print(f"age:{user_info['Age']}")
    print(f"email:{user_info['email']}")     
user_info = collect_user_id()

main(user_info)