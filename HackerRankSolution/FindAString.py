def count_string(main_str,sub_str):
    count = 0
    n = len(main_str) - len(sub_str) + 1
    for i in range(n):
        if(main_str[i:len(sub_str)+i] == sub_str):
            count = count+1
    return count
main_str = input()
sub_str = input()
res = count_string(main_str,sub_str)
print(res)