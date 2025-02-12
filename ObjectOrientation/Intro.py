class Student:
    def learn(self):
        print("Inside Learn Method")
    def play(self):
        print("Inside Play Method")
s1 = Student()
s1.learn()
# Error s1.play() # Takes 0 positional arguments but 1 was given

# Constructor
class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def work(self):
        print(f"{self.name} is working ")
e1 = Employee('Sagar', 22)
e1.work()