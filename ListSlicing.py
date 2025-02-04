# List_name[Start:End-1:Steps]:
li1 = [10,20,30,40,50,60]
sub_list = li1[0:4:1] # sub_list from Main_list , Slice means Cut
print(sub_list) # [10, 20, 30, 40]
# It start from first list and end list 4-1=3

sub_list1 = li1[::] # Corner Case 
print(sub_list1) # [10, 20, 30, 40, 50, 60] Print including last one. 

sub_list2 = li1[1::]
print(sub_list2) # [20, 30, 40, 50, 60]

sub_list3 = li1[::2]
print(sub_list3) # [10, 30, 50]

reverse_list = li1[::-1] # to reverse List
print(reverse_list) # [60, 50, 40, 30, 20, 10]

print(li1[-1::]) # [60] To Print Last Element

'''
Q. What is List Slicing?
-> is used to create sub_list from main List.
Syntax: List_name[Start:end-1:Steps]
Reverse List : [::-1]
last ele : [-1::]
'''