'''
1.In dict we cannot store duplicate keys. # 'name' : We cannot duplicate it.
2.In dict we can store duplicate values.
3.dict is mutable.
'''
d1 = {'name':'Sagar', 'age':27, 'phone':5986}
print(d1) # {'name': 'Sagar', 'age': 27, 'phone': 5986}

# Before Python 3.18 it is unordered collection of data.
# Duplicate Keyword are not allowed.

d1 = {'name':'sagar', 'age':27, 'Phone': 23456, 'age': 27}
print(d1, type(d1)) # {'name': 'sagar', 'age': 27, 'Phone': 23456} <class 'dict'>

d1['name'] = 'Kshatriya'
print(d1) # {'name': 'Kshatriya', 'age': 27, 'Phone': 23456}

marks = {'Sci':85,'Maths':85} # Allowed

# Function()
for i in d1.keys():
    print(i) # name age Phone Kshatriya
for i in d1.values():
    print(i) # 27 23456
for i in d1.items():
    print(i) # ('name', 'Kshatriya') ('age', 27) ('Phone', 23456)