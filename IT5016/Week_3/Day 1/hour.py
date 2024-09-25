def get_minutes(minutes):
    total = minutes / 60 
    return total

# hours= float(input("Enter Hours: "))
minutes= float(input("Enter Minutes: "))


total_minutes= get_minutes(minutes)
print("The total hour is ", total_minutes)