#If String is holding integer then it can be Converted into int.
a = '30'
print(a, type(a))
b = int(a)
print(b,type(b))

#string to integer conversion is not allowed
x = 'Kod'
print(x,type(x))
# y=int(x)
# print(y,type(y))

# p = float(input("Enter float type data"))
# print(p,type(p))

q = 12
print(q,type(q))
q=bool(q)
print(q,type(q))

# 1.While converting int to bool for all non zero values we will get True
# 2.While Converting int to bool for 0 and empty

#Taking float value from user and converting it into int.
value = int(float(input('Enter price:Float value')))
print(value, type(value))