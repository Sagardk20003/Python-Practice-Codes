# List(Iterable_object):
# li1  = list(44.22) # Error
# print(li1) # Error
li1 = list('Kod')
print(li1) # ['K', 'o', 'd']

li2 = list((10,20))
print(li2) # [10, 20]

li3 = list({100,200})
print(li3) # [200, 100]

li4 = list({'name':'Sagar','age':21})
print(li4) # 

li5 = list(range(1,10))
print(li5) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Tuple(Iterable_object):
tup1 = tuple([10,20,30])
print(tup1) # (10, 20, 30)

tup2 = tuple({100,200})
print(tup2) # (200, 100)

tup3 = tuple(range(1,11))
print(tup3) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

tup4 = tuple('kodnest')
print(tup4) # ('k', 'o', 'd', 'n', 'e', 's', 't')

tup5 = tuple({'name':'sagar','age':22})
print(tup5) # ('name', 'age')

# Set(Iterable_object): If needed add all the above object 
s1 = set([10,20,30,30])
print(s1) # {10, 20, 30}

# dict(iterable_Object:Key:Value) :
d1 = dict([['name','sagar'],['age',22]])
print(d1) # {'name': 'sagar', 'age': 22}