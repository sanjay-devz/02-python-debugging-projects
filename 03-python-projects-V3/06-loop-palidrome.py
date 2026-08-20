name = input("Enter Word:")
orignal = name


new_name = ""


for i in range(len(name)-1,-1,-1):
   new_name += name[i]




if new_name == orignal:
    print("its a palidrome")

else:
    print("its not a palidrome")

    
