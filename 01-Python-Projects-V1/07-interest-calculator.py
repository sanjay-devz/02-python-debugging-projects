while True:
    
    try:
        print("\n\t-------Welcome To Intrest Calculator-------")
    
        print("\t\t\t---Menu---")
        print("\n01-Simple Interest  \n02-Total Amount \n03-Compund Interest \n04-Monthly EMI \n05-Profit Percentage \n06-Disount Percentage \n07-Quit\n ")
       
        choice = int(input("Enter Your Choice [0,1,2,3,4,5,6,7]: "))

        if choice in [1,2,3,4,5,6,7]:
                if choice == 7:
                       
                       print("-" * 30)
                       print("Goodbye!!\nHave A Nice Day...")
                       print("-" * 30)
                       break
                
                
                elif choice == 1:
                    print("--Simple Interest--")
                    P = float(input("Enter The Principle Amount: "))
                    R = float(input("Enter Interest Rate: "))
                    T = float(input("Enter The Number of Years: "))

                    Rate = R / 100
                    SI = (P * Rate * T ) 

                    print("-" * 29)
                    print(f"The Simple Interest isर{SI:.2f}/-")
                    print("-" * 29)
                
                elif choice == 2:
                     print("--Total Amount--")
                     P = float(input("Enter The Principle Amount: "))
                     R = float(input("Enter Interest Rate: "))
                     T = float(input("Enter The Number of Years: "))

                     Rate = R / 100
                     SI = (P * Rate * T ) 
                     A = P + SI

                     print("-" * 29)
                     print(f"The Total Amount is र{A:.2f}/-")
                     print("-" * 29)

                elif choice == 3:
                     print("--Compound Interest Amount--")
                     P = float(input("Enter The Principle Amount: "))
                     R = float(input("Enter Interest Rate: "))
                     T = float(input("Enter The Number of Years: "))
                    
                     Rate =  R / 100
                     CI = P * (1 + Rate) ** T - P
                     CA =  P * (1 + Rate) ** T

                     print("-" * 29)
                     print(f"The Compound Interest is र{CI:.2f}/-")
                     print(f"The Compound Amount is र{CA:.2f}/-")
                     print("-" * 29)

                elif choice == 4:
                     print("--Monthly EMI--")
                     P = float(input("Enter The Principle Amount: "))
                     R = float(input("Enter The Annual Interest Rate: "))
                     T = float(input("Enter The Numbers of Years: "))

                     n = T * 12
                     r = R / (12 * 100)
                     EMI = (P * r * (1+r)**n ) / ((1 + r)**n-1)

                     print("-" * 29)
                     print(f"The Monthly EMI is र{EMI:.2f}/-")
                     print("-" * 29)
                     
                elif choice == 5:
                     print("--Profit Percentage--")
                     CP = float(input("Enter The Cost Price: "))
                     SP = float(input("Enter The Selling Price: "))
                     
                     profit = ((SP - CP) / CP) * 100 

                     print("-" * 29)
                     print(f"The Profit is {profit:.2f}%")
                     print("-" * 29)

                elif choice == 6:
                     print("--Discount Percentage--")
                     MP = float(input("Enter The Market Price: "))
                     SP = float(input("Enter The Selling Price: "))

                     discount = ((MP - SP) / MP ) * 100
                     print("-" * 29)
                     print(f"  The Discount is {discount:.2f}%",)
                     print("-" * 29)

                else:
                     print('The Inside Else Block is Executing!! why??')
                     
        else: 
            print("Invalid Choice Enter Choice \nIn This List --> [1,2,3,4,5,6,7]")
            print("-" * 30)
            break
    except ValueError:
         print("\n","-" * 38)
         print("The Calculator only iterate Numbers\nInvalid Input Values \nEnter The Valid Input Values\n\n\t Try Again....!\n") 
         print("-" * 38) 
         break




             
                     

                        
                    
                            
        
        
            

