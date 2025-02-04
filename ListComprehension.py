# Without List Comprehension
li1 = [1,2,3,4,5] # for Square of list
print(li1) # [1, 2, 3, 4, 5]
sq_li = []
for i in li1:
    sq_li.append(i**2)
print(sq_li) # [1, 4, 9, 16, 25]

#With List Comprehension

li1 = [1,2,3] # Duplicate
new_li = [i for i in li1]
print(new_li) # [1, 2, 3]
sq_li = [i**2 for i in li1] # Square Root
print(sq_li) # [1, 4, 9]
new_li2 = [ele+2 for ele in li1] # Element adding
print(new_li2) # [3, 4, 5]

# When we have only if part then write it after for loop
# By default it return value
li1 = [1,2,3,4,5]
even = [i for i in li1 if i%2==0]
print(li1) # Even

# If and else both in list Comprehension.
li = [1,2,3]
# expected_output = ['odd','even','odd']

# When we have if-else both to write it before for loop
even_odd = ['even' if i%2==0 else 'odd' for i in li]
print(even_odd) # ['odd', 'even', 'odd']

# Nested for loops inside list Comprehension
li = [[10,20],[30,40],[50,60]]
new_li = [ele for sublist in li for ele in sublist]
print(new_li) # [10, 20, 30, 40, 50, 60]