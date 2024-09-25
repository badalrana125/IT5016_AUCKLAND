def ask_simple_intrest():
    principal= int(input("Enter principal: "))
    Time= int(input("Enter Time period: "))
    Rate= int(input("Enter the rate: "))
    ask_simple_intrest= (principal*Time*Rate)/100
    amount= ask_simple_intrest + principal
    print("The simple intrest is", ask_simple_intrest,"The Total amount including Simple Intrest",amount)
ask_simple_intrest()
     