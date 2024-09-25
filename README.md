"""
Description: A program to collect user information
Author: Aashish Sagar Basyal
"""

#Collect the user informations
def collect_user_information(id_counter):
    user_name = input("ENTER THE NAME OF THE STUDENT:")
    user_age = input("Enter the age of the student:")
    user_email = input("Enter the email of the student:")

#To generate unique id
  unique_id = id_counter+1
  id_counter = unique_id

#to display
  print("User Information")
  print(f"Name:{user_name}")
  print(f"Age: {user_age}")
  print(f"email:{user_email}")
  print(f"Unique_id :{id_counter}")

  return user_email,user_age,user_name,id_counter

def  calculate_total_amount():
    tot_amount =0.0
    while True:
        item_input= input("enter the name of the item(or type 'finish' to end ):")
        
  if item_input.lower() == 'finish':
            break

  try:

  price = float(input(f"enter the price of the item'{item_input}':"))
  tot_amount += price
        except ValueError:
            print("Invalid input, please enter a value number.")

  return tot_amount
 def categorize_request(tot_amount):

  if tot_amount < 150:
        category = "Low"
        recommendation = "Proceed with standard processing"
        print(recommendation)
  else:
        category =" high"
        recommendation = "Review for ptotential discount"
        print(recommendation,category)

  return category,recommendation

def create_detailed_report(id_counter,user_name, user_age,user_email,tot_amount,category, recommendation):

  print("Detailed Report")
  print(f"Unique ID:{id_counter} ")
  print(f"Name: {user_name}")
  print(f"Age:{user_age}")
  print(f"Email:{user_email}")
  print(f"Total amount:{tot_amount:.2f}")
  print(f"Category:{category}")
  print(f"Recommendation :{recommendation}")

 # Main function to execute the program
def main():
    id_counter = 5000
    id_counter, user_name , user_age, user_email = collect_user_information(id_counter)
    tot_amount = calculate_total_amount()
    category,recommendation = categorize_request(tot_amount)
    create_detailed_report(id_counter,user_name, user_age,user_email,tot_amount,category,recommendation)
main()

____Software Development Principles and explanation related to my code:

1.DRY (Don't Repeat Yourself):
I strongly avoid repeated writing my code. For example, I saw that I was printing user information repeatedly from various parts of a program. To address this, I came up with another function called print_user_info(). Thus, instead of having to rewrite the same print statements all over the code, I can control how the user details are presented from one place easily. It is useful because it keeps my code cleaner and more efficient.
def print_user_info(user_name, user_age, user_email, id_counter):def print_user_info(user_name, user_age, user_email, id_counter):
print("User Information")
print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"Email: {user_email}")
print(f"Unique ID: {id_counter}")

2.KISS (Keep It Simple, Stupid):
The best strategy I have learned and adapted is simplicity. That is why I want each function to be clear and serve only one purpose. I understand that it’s unproductive to give them several tasks at once; instead, all the tasks serve a specific function. As a result, using such names helps me in reading my own code since it is well arranged as well as easy to understand when making additions or changes in future.

3.Single Responsibility Principle (SRP):
You see, nothing in any function I write does anything but one particular thing. For instance, the function collect_user_information() is only responsible for collecting the information of the user and calculate_total_amount() is only responsible for calculating total amounts. Such division of responsibilities serves to prevent the confusion as well as to simplify the process of debugging or improving a specific segment in the code, if necessary.

4.Separation of Concerns:
I have separated my code into an easily understandable structure where two functions don’t overlap. I decompose the sets of input collection, calculation, categorization, and reporting into different functions to ease my ability in managing and testing them. This way there is no hazy area that I can’t identify if something is wrong or needs some change.

5.YAGNI (You Aren't Gonna Need It):
I try to keep telling myself not to complicate the situation anymore than it is already that is another thing that I need to ensure that I do not introduce unnecessary features. I try to develop what for the present functionality is necessary. This particular principle is useful in that it keeps me from deviating from the objective and over-complicating my code needlessly.

6.Open/Closed Principle (OCP):
My code is a perfect paradigm for a future-oriented approach. It’s designed to allow me to make modifications and unleash new features while not affecting the other ones. For instance, should I wish to add new fields into collect_user_information() function the extension is very easy. In the same respect, if I desire to incorporate the functionality to add new categories in the categorize_request() function, I can easily include that without manipulation of that which exists. This makes my code more dynamic for future calls.
In my code:
Extending the collect_user_information() function to collect new fields (like address or phone) without changing its original structure.
Adding new categories in categorize_request() by introducing additional conditions without modifying the existing logic.
