
try: 
    converted_temp = None
    temperature = float(input("Enter the Temperature: "))
    temperature_unit = input("Enter the Unit |C/F|: ").upper()

    if temperature_unit == "C":
        converted_temp = (temperature * 9/5 ) + 32
        temperature_unit = "F"
        #"The Celsius -> Fahrenheit: {Fahrenheit}"

    elif temperature_unit == "F":
        converted_temp = (temperature - 32) * 5/9
        temperature_unit = "C"
       # "The Fahrenheit -> Celsius: {Celsius}"
    
    else:
        print("\n==> Invalid Unit Entered <==\n\n\t+----Try Again----+")
        
    
except ValueError:
    print("The Temperature can only iterate float or int\nThe input cannot be iterated")


finally: 
    if converted_temp is not None:
        print("")
        print("-" * 38)
        print(f"  The Converted Temperature:{converted_temp:.2f}°{temperature_unit}")
        print("-" * 38)
        print("")

