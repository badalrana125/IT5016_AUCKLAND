def get_minutes(hours, minutes):
    total = hours * 60 + minutes 
    return total

hours= float(input("Enter Hours: "))
minutes= float(input("Enter Minutes: "))


total_minutes= get_minutes(hours,minutes)
print("The total minutes is ", total_minutes)

