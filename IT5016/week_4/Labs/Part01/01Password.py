"""
A simple password input system using while loop
"""

def password_attempt_system():
    correct_password= "python@321"
    attempts= 0
    max_attempts= 5
    while attempts< max_attempts:
        entered_password= input("Enter your Passwprd: ")
        if entered_password == correct_password:
            print("Access Granted!...You entered correct password.")
            break
        else:
            attempts += 1
            print(f"Access Denied!..You have {max_attempts- attempts} attempts left.")
            
    if attempts == max_attempts:
        print("Opps! you have no more attempts left..")
        
password_attempt_system()
            
        