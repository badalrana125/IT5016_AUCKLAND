def BMI(weight, height):
    # height_in_m= height/100
    bmi= weight/(height/100)**2
    return bmi
    

weight = int(input("Enter weight: "))
height= int(input("Enter height: "))



# cm_to_m=
print(BMI(weight,height))