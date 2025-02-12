print('c'.islower()) # true
print('Kodnest'.isupper()) # False

def swapcase(s):
    sample = ''
    for i in s:
        if i.islower():
            sample = sample + i.upper()
        else: 
            sample = sample + i.lower()
    return sample
sample = input()
result = swapcase(sample)
print(result)