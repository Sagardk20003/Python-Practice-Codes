'''
a = input()

n = input('Enter the Num 1')
print('value of num1 is:',n,'Data Type of Num1 is:',type(n))

# input() will always takes an input as a String 
'''
# TypeCasting
num1 = int(input('Enter the num1'))
num2 = int(input('Enter the num2'))
print(f"Addition of {num1} and {num2} is {num1+num2}")

# Division Result will always be of type float.
num1 = int(input('Enter the num1')) # 20
num2 = int(input('Enter the num2')) # 10
print(f"Addition of {num1} and {num2} is {num1+num2}") # 30
print(f"Subtraction of {num1} and {num2} is {num1-num2}") # 10
print(f"Multiplication of {num1} and {num2} is {num1*num2}") # 200
print(f"Division of {num1} and {num2} is {num1/num2}") # 2.0