class employee_details:
    #creating a constructor.
    def __init__(self,name,eid,salary):
        self.name = name
        self.eid = eid
        self.salary = salary

    #createing a __str__
    def __str__(self):
        return f"Employee Name: {self.name}\nEmployee ID: {self.eid}\nEmployee Salary: {self.salary}"
    

employee1 = employee_details("Sanjay","ADS785","25,000")

print(employee1)
        
        
