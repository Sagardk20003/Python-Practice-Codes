# for control_variable in iterable_object

for i in 'Sagar':
    print(i, end="-")
print()
    
for j in [10, 20, 30]:
    print(j+5, end=" ")
print()
    
for num in range(1,11):
    print(num, end=',') 
print()
    
for num in range(11,21,2): #Steps means continue with 2 steps after count
    print(num,end=",")
print()

for num in range(5):
    print(num,end=" ")
print()

#WAP to Print all Even Numbers from 1-10
for num in range(1,11):
    if(num%2==0):
        print(num, end=" ")
print()

# While Loop
i = 0
while(i<10):
    print(i+100, end=" ")
    i = i+1
print()

#WAP to Print Number from 1 to 10, if Numbers is 6 then skip Printing.
# While Loop
i = 1
while(i<11):
    if(i==6):
        pass # Pass Means Empty Class Empty Method, Which i don't what to write
    else:
        print(i,end=" ")
    i = i+1
print()
# For Loop
for i in range(1,11):
    if(i==6):
        continue
    print(i,end=" ")
print()

#WAP to Print Number from 1 to 10, if Numbers is 5 then stop Printing.
# While Loop
i = 1
while(i<11):
    if(i==5):
        break
    else:
        print(i,end=" ")
    i = i+1
print()
# For Loop
for i in range(1,11):
    if(i==5):
        break
    print(i,end=" ")
print()