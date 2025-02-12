''' Instance Variable are such variable which are present or which are assigned specifically to that particular instance only
'''
class Employee:
    company_name = 'code' # class Based Variable
    def __init__(self,name,age,designation):
        self.name = name
        self.age = age
        self.designation = designation
    def login(self,time):
        print(f"{self.name} logged in at {time}")
    def logout(self,time):
        print(f"{self.name} logged out at {time}")
    def work(self,hours):
        print(f"{self.name} worked for {hours}")
    def getDetails(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee age: {self.age}")
        print(f"Employee designation: {self.designation}")
# Creating Objects
Emp1 = Employee('Sagar',22,'Software Developer trainee')
Emp2 = Employee("Meghana",24,'A&Q control')
Emp1.getDetails()
Emp2.getDetails()