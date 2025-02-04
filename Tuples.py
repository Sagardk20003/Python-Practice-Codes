'''
1.In Tuple we can store Homogeneous as well as Heterogeneous Data.
2.In Tuple we can store Duplicates.
3.Tuples are ordered collection of data.
4.Tuples are Immutable: once we declare the tuple we cannot modify it.
'''

tup1 = (10,22.55,'Sagar',True,10)
print(tup1) # (10, 22.55, 'Sagar', True, 10)

# append(), remove(), pop(), del Var_name[] -> Not Allowed.
print(tup1[2]) # Sagar

# del -> Deletes the Complete tuple List.
del tup1

# Create a singleton Tuple:
tup = (10,) # CornerCase -> (10) int DataType
print(tup,type(tup)) # (10,) <class 'tuple'>

new_tup = (10,20,30,40)
# ele_1 = new_tup[0]
# ele_2 = new_tup[1]
#Unpacking of tuple
ele1,ele2,ele3,ele4 = new_tup
print(ele1,ele2,ele3,ele4) # 10 20 30 40
print('value of ele',ele1) # 10