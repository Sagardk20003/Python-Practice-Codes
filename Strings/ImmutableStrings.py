s1 = 'Kodnest'
s1.upper()
print(s1)

''' 
String are Immutable:

1. Once we declare the strings we cannot modify it, 
if we try to modify the String, 
it will create new String.

2.If new string doesn't have any reference variable then it will be removed. 
'''
s1 = 'Kodnest'
s1 = s1.upper()
print(s1)

s1 = 'K'
print(s1, id(s1))

s1 = 'Hello'
s2 = 'World!'
print(s1,id(s1))
print(s2,id(s2))

print(s1[0]) # H
print(s1[-1]) # o

print('s1 Id of H:',id(s1[0]))
print('s2 Id of W:',id(s2[0]))

print('s1 Id of o:',id(s1[-1]))
print('s2 Id of o:',id(s2[1]))
print('s2 Id of o:',id(s2[3]))

print('s1 Id of l:',id(s1[2]))
print('s1 Id of l:',id(s1[3]))