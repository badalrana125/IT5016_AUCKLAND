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