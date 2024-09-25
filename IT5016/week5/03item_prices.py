def categorize_request():
    Total_price= float(input("Enter a price: "))
    if Total_price < 150: 
        category = "low"
        recommend = "procced witn standard processing."
    else:
        category = "High"
        recommend= "Review for potential discount."

    print("Request Summary: ")
    print(f"Total amount: ${Total_price}")
    print(f"Category:{category}")
    print(f"Recommend:{recommend}")

categorize_request()