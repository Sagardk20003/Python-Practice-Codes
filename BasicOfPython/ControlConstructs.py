'''
Types of Control Construct:
1.Conditional: if-else, if-elif
2.Looping: for, while
Jumping: break, continue, pass
'''

def checkAge(age):
    if(age>18):
        print("Age is Greater than 18")
    else:
        print("Age is not greater than 18")
checkAge(18)

'''
Write a program(WAP) to display 
'Child' if age is below 18,
'Adult' is age is above 18,
'Senior Citizen' if age is above 65
'''
def checkAge(age):
    if (age>65):
        print("Senior Citizen")
    elif(age>=18):
        print("Adult")
    else:
        print("Child")
checkAge(int(input('Enter the Age: ')))