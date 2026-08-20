print("=========================================")
print("         ADVANCE TEMPERATURE             ")
print("=========================================")
print("")

while True:
    try:
    
        choice = input("Enter => I To Continue (or) Q for Quit: ").upper()

        if choice == "Q":
            print("GoodBye!!\nHave A Nice Day..")
            
                # Input block if user continues..
        if choice == "I":
            temperature = float(input("Enter Temperature:"))

         
            current_unit = input("Current Unit: ").upper()
            convert_unit = input("Convert Unit: ").upper()
            converted_temp = None

            if current_unit in ["C","F","K"]:
                
                if convert_unit in ["C","F","K"]:

           
            
                    
                    #conditional block for unit and temperature conversion.
                    if current_unit == convert_unit:
                        print(f"Temperature Remains Same because\n{current_unit} Is Same As{convert_unit}\nTemperature = {termperature}°{current_unit}")
                    
                    elif current_unit == "C" and convert_unit == "F":
                        converted_temp = (temperature * 9/5 ) + 32
                    
                    elif current_unit == "C" and convert_unit == "K":
                        converted_temp = (temperature + 273.15)

                    elif current_unit == "F" and convert_unit == "C":
                        converted_temp = (temperature - 32) * 5/9

                    elif current_unit == "F" and convert_unit == "K":
                        converted_temp = (temperature - 32) * 5/9 + 273.15

                    elif current_unit == "K" and convert_unit == "C":
                        converted_temp = temperature - 273.15

                    elif current_unit == "K" and convert_unit == "F":
                        converted_temp = (temperature - 273.15) * 9/5 + 32

                    else:
                        pass
            
            

                
                print("")
                print('Temperature only convert into\n[C/F/K] => Enter The Valid Input')       
                print("")     
                

    except ValueError:
        print('Temperature only contain numeric value')





            
    


            
        
    
    