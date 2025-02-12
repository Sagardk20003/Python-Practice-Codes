def mutate_string(string,position,character):
    li = list(string)
    li[position] = character
    string = "".join(li)
    return string
string = input()
position,character = input().split()
result = mutate_string(string,int(position),character)
print(result)