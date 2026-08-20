"""class Bank_account:
    def __init__(self,help,getting):
        self.help = help 
        self.getting = getting
        return help 



bank = Bank_account("get","in")

   
class bank:
    def __init(self,name):
        self.name = name 
        


bank_1 = bank("Sanjay")
 
class student:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "Student Name:" + self.name

s1 = student("sanjay")
print(s1)
 """

class bank:
    def __init__(self,name,phone_no,account_no):
        self.name = name
        self.phone_no = phone_no
        self.account_no = account_no

    def __str__(self):
        return f"Name:{self.name}\nphone:{self.phone_no}\nAccount No: {self.account_no}"
    

bi = bank("sanjay",7904203759,123456789123589542)

print(bi)
        