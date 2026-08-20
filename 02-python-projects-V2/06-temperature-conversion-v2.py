while True:
    try:
        choice = input("Enter => I To Continue (or) Q for Quit: ").upper()
        if choice == "Q":
            print("The Program Ends\nGood Bye..!")
            break
        elif choice == "I":
            temperature = float(input("Enter Temperature:"))
            current_unit = input("Current Unit: ").upper()
            convert_unit = input("Convert Unit: ").upper()

            if current_unit == convert_unit:
                print(f"Temperature Remains Same because\n{current_unit} Is Same As {convert_unit}\nTemperature = {temperature}°{current_unit}")
            elif current_unit == "C" and convert_unit == "F":
                converted_temp = (temperature * 9/5) + 32
                print(f"{temperature}°C = {converted_temp:.2f}°F")
            elif current_unit == "C" and convert_unit == "K":
                converted_temp = temperature + 273.15
                print(f"{temperature}°C = {converted_temp:.2f}°K")
            elif current_unit == "F" and convert_unit == "C":
                converted_temp = (temperature - 32) * 5/9
                print(f"{temperature}°F = {converted_temp:.2f}°C")
            elif current_unit == "F" and convert_unit == "K":
                converted_temp = (temperature - 32) * 5/9 + 273.15               
                print(f"{temperature}°F = {converted_temp:.2f}°K")
            elif current_unit == "K" and convert_unit == "C":
                converted_temp = temperature - 273.15
                print(f"{temperature}K = {converted_temp:.2f}°C")
            elif current_unit == "K" and convert_unit == "F":
                converted_temp = (temperature - 273.15) * 9/5 + 32
                print(f"{temperature}K = {converted_temp:.2f}°F")
            else:
                print("Invalid unit selection")
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid temperature. Please enter a number.")




