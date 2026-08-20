class wallet:

    def __init__(self,owner,deposit,withdraw):
        self.owner = owner
        self.__money = 500
        self.deposit = deposit
        self.withdraw = withdraw

    def get_money(self):
        total = self.__money + self.deposit - self.withdraw
        return total
        
    def __str__(self):
        return f"Total: {self.get_money()}"
        
wallet1 = wallet("sanjay",200,400)

print(wallet1)

        