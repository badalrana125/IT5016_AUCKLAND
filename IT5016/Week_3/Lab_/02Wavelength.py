def light_rages():
    message = "Welcome to Wavelength to colour Converter>>"
    print(message)
    try:
     wavelength = int(input("Please enter an integer wavelength between 380 and 750>>>"))
    except ValueError:
     print("error: Please enter the valid wavelength: ")

    print(f"Thank You, the wavelength that you entered is:{wavelength}")
    message_02= "The colour for this wavelegth is..."
    if 620<=wavelength<750:
       color = "red"
    elif 590<=wavelength<620:
        color = "orange"
    elif 570<=wavelength<590:
        color="Yellow"
    elif 495<=wavelength<570:
        color="Green"
    elif 450<=wavelength<495:
        color="Blue"
    elif 380<= wavelength<450:
        color="Voilet"
    else:
        print("You entered an error number")
    print(f"The color corresponding to the wavelength {wavelength} nm is: {color}")
light_rages()
