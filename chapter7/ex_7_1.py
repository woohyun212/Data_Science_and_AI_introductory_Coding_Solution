fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'melon']
largest_str = []
largest_str_len = len(max(fruit_list))
for i in fruit_list:
    if len(i) == largest_str_len:
        largest_str.append(i)
for i in largest_str:
    fruit_list.remove(i)
print(f"가장 길이가 긴 문자열 : ", end='')
for i in largest_str:
    print(i, end=" ")
print(f'\nfruit_list = {fruit_list}')
