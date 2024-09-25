def collect_user_information(id_counter):
    user_name = input("ENTER THE NAME OF THE STUDENT:")
    user_age = input("Enter the age of the student:")
    user_email = input("Enter the email of the student:")

  unique_id = id_counter+1
  id_counter = unique_id
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

def main():
    id_counter = 5000
    id_counter, user_name , user_age, user_email = collect_user_information(id_counter)
    tot_amount = calculate_total_amount()
    category,recommendation = categorize_request(tot_amount)
    create_detailed_report(id_counter,user_name, user_age,user_email,tot_amount,category,recommendation)
main()

____Software Development Principles and explanation related to my code:

1. DRY (Don't Repeat Yourself)
Principle: Do not repeat the same code as it creates several instances of the same logic for its execution.
In the code: Some of the segments of codes that could be improved include The print() statements that convey user information could be encapsulated in a different function to save on time instead of being repeated. For example, it is better to create a function known as print_user_info() that will help in avoiding repetition when printing user details.
Improvement:
def print_user_info(user_name, user_age, user_email, id_counter):def print_user_info(user_name, user_age, user_email, id_counter):
print("User Information")
print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"Email: {user_email}")
print(f"Unique ID: {id_counter}")

2. KISS is actually an acronym for ‘Keep It Simple, Stupid’.
Principle: The code must be simple; just as simple as possible. Do not pack each function with features, and steps to complete the job, instead make every function clean and basic.
In the code: There is no significant overlapping of tasks in your code and each function, what you have is the representation of this principle. But it would become necessary to make certain that you do not add many conditions or unnecessarily complicate it while extending it.
3. Single Responsibility Principle (SRP)
Principle: Single Responsibility Principle: Every function or class should do only one thing or be change for only one reason.
In the code: All the functions you have defined (collect_user_information, calculate_total_amount, categorize_request, create_detailed_report) have simple and clear purpose, which is perfect. Here there is no problem you are following the SRP in the most proper manner.

4. Separation of Concerns
Principle: There should be conceivably corresponding division of labors and responsibilities in the different sections of the code such that issues and functionalities are handled uniquely and do not overlap.
In the code: You have split input collection, amount calculation, request categorisation and report generation in to different functional areas as per this principle. This makes the make the code more manageable for testing and maintenance.

5. YAGNI means You Aren’t Gonna Need It or there is no need to build something unless it is needed.
Principle: Never build features unless it’s indispensable to do so. Always remember to not put in things that are not needed at the present time such as adding features or putting in a logic.
In the code: This principle does not pose any problems to your code since all the logic carried in it seems to be useful in one way or the other.

6.Open/Closed Principle (OCP) Summary
The Open/Closed Principle ensures that code is designed to be easily extended with new features without altering the existing functionality. This keeps the core stable and reduces the risk of introducing bugs.

In my code:

Extending the collect_user_information() function to collect new fields (like address or phone) without changing its original structure.
Adding new categories in categorize_request() by introducing additional conditions without modifying the existing logic.
