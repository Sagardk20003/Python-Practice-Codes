'''
1.In set we can store homogeneous data as well as heterogeneous data.
2.In set is an unordered collection of data.
3.set does not support indexing of data.
4.In set we cannot store duplicates.
5.sets are Mutable.
'''

s1 = {10,True,'Kodnest',10,20,55.44}
print(s1,type(s1)) # {True, 20, 55.44, 10, 'Kodnest'} <class 'set'>
# print(s1[0]) # Error

# add(): used to add an element in the set.
s1.add(500)
print(s1) # {True, 20, 500, 55.44, 10, 'Kodnest'}

#remove():
s1.remove(55.44)
print(s1) # {True, 20, 500, 10, 'Kodnest'}

# pop(): Without index will delete and return one element.
s1.pop() # S1.pop(Index) is not allowed
print(s1) # {20, 500, 10, 'Kodnest'}

poped_ele = s1.pop()
print(poped_ele) # true # 20

del s1 # -> delete every data inside s1
#del s1[2] # Error