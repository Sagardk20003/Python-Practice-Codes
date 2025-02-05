'''
1.In List we can store Homogeneous as well as Heterogenous Data.
2.In List we can store Duplicate Values.
3.List is an ordered collection of Data: Order of insertion will remain as it is in the output.
4.Lists are Mutable: Once we declare the List we can Modify it.
'''

li1 = [10,20,44.45,True,'Sagar',20]
print(li1, type(li1))

# append(): Will add element at the end of the list. only one data can be added once.
li1.append(300)
print(li1) # [10, 20, 44.45, True, 'Sagar', 20, 300]

# insert(index, element): Adds or Inserts an element at specified index.
li1.insert(1,15)
print(li1) # [10, 15, 20, 44.45, True, 'Sagar', 20, 300]

# remove(ele): remove the first occurrence of the dpecified element.
li1.remove(20)
print(li1)

# in and not in operator:(Membership operator)
print(1000 in li1) # false
print('Sagar' in li1) # True

# pop(): Without arguments will delete and return last element from list.
li1.pop()
print(li1) # [10, 15, 44.45, True, 'Sagar', 20]

removed_ele = li1.pop()
print(removed_ele) # 20

# pop(Index): with arguments will delete the elements at specific index.
removed_ele = li1.pop(4)
print(removed_ele) # Sagar
print(li1) # [10, 15, 44.45, True]

# del 'KeyWord': if you don't want to know the history of you delete you use del.
del li1[1]
print(li1) # [10, 44.45, True] 

# del li1 -> Completely delete the list which is included or stored in this List.