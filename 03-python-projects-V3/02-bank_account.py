class Bank_account:
    def __init__ (self):
        print("the constructor was created!!")
    coustomer_name = ""
    Balance = 0.0
    account_number = 0
    def account_status(self):
        return "The account is Valid!!"
   



Sanjay_bank = Bank_account()

Sanjay_bank.coustomer_name = "Sanjay"
Sanjay_bank.Balance = 2334
Sanjay_bank.account_number = 12312312131213

print(Sanjay_bank.coustomer_name)
print(Sanjay_bank.Balance)
print(Sanjay_bank.account_number)
x = Sanjay_bank.account_status()
print(x)


gopal_account = Bank_account()
gopal_account.coustomer_name = "Gopal kumar"
gopal_account.Balance = 390000
gopal_account.account_number = 124589780163
y = gopal_account.account_status()
print(gopal_account.account_number)
print(gopal_account.Balance)
print(gopal_account.coustomer_name)
print(y)



