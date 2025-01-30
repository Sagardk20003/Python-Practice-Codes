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