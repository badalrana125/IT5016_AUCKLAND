def earthquake_magnitude ():
    message= "The Earthquake is"
    # magnitude_= "Please enter the earthquake magnitude: "
    magnitude_2 = float(input("Please enter the earthquake magnitude: "))
    #   return earthquake_magnitude

    if magnitude_2 <2.0:
       print(message, "Micro")
    elif  2.0 <= magnitude_2 <3:
       print(message,"Very minor")
    elif  3.0<= magnitude_2 <4.0:
       print (message, "Minor")
    elif  4.0<= magnitude_2 <5.0:
       print(message,"Light")
    elif 5.0<=magnitude_2<6.0:
       print(message,"Modrate")
    elif  6.0<=magnitude_2<7.0:
       print(message,"Strong")
    elif 7.0<=magnitude_2<8.0:
       print(message, "Major")
    elif 8.0<=magnitude_2<10:
       print(message,"Great")
    else:
       print(message,"Meteoric")
earthquake_magnitude()