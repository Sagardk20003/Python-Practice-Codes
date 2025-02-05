print('*') # *
print()

N = 5
print('*' * N) # *****
print()

rows = 5
col = 5
#Nested For Loop
for i in range(rows):
    for j in range(col): # default of star is 0, so Col-1 = Means 5 - 1 = 4
        print('*',end = '')
    print() # default '/n'
print()

for i in range(rows):
    for j in range(i+1):
        print('*',end = '')
    print()
print()

for i in range(rows):
    for j in range(i,rows):
        print('*',end = '')
    print()
print()

for i in range(rows):
    for j in range(i+1):
        print('*',end = '')
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print('*',end = '')
    print()
print()

for i in range(rows):
    for j in range(i+1):
        print('*',end = '')
    for j in range(i,rows-1):
        print(' ',end = '')
    for j in range(i,rows-1):
        print(' ',end = '')
    for j in range(i+1):
        print('*',end = '')
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print('*',end = '')
    for j in range(i+1):
        print(' ',end = '')
    for j in range(i+1):
        print(' ',end = '')
    for j in range(i,rows-1):
        print('*',end = '')
    print()
print()

for i in range(rows):
    for j in range(i,rows):
        print(' ',end = '')
    for j in range(i):
        print('*',end = '')
    for j in range(i+1):
        print('*',end = '')
    print()
for i in range(rows):
    for j in range(i+1):
        print(' ',end = '')
    for j in range(i,rows-1):
        print('*',end = '')
    for j in range(i,rows):
        print('*',end = '')
    print()