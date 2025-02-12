# alnum(): checks for alpha or numbers
print('Kodnest1234'.isalnum())
print('Kodnest1234*'.isalnum())
print('kodnest'.isalnum())

print('kodnest12'.isalpha())
print('kodnest'.isalpha())

print('12'.isdigit())

print('apple'.islower())
print('apple'.isupper())

print(any([10,20]))
print(any([True,False,False]))
print(any([False,False]))
print(any([0]))
print(any([10]))

#------------------------- LOGIC ------------------------#

s = input()
print(any([i.isalnum() for i in s]))
print(any([i.isalpha() for i in s]))
print(any([i.isdigit() for i in s]))
print(any([i.islower() for i in s]))
print(any([i.isupper() for i in s]))