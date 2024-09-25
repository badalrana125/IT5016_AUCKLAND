import random
def user_number_guess(computer_num):
   prompt= "Enter your guess(1-10):"
   number_guesses= 0
   number=0
   while number!= computer_num:
       number = int(input(prompt))
       number_guesses +=1
       if number< computer_num:
           print("too low")
       elif number> computer_num:
           print("too High")
       else:
           print(f"Correct! number of Guess: {number_guesses}")

 


#    def user_numb

def main():

    user_number_guess(random.randrange(1,10))
main()
