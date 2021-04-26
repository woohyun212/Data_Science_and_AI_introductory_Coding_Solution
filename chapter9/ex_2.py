import re

string = input('문자열을 입력하시오 : ')
up = re.findall("[A-z]", string)
low = re.findall("[a-z]", string)
print(''.join(low+up))
# for i in string:
#     if i.isupper():
#         cap.append(i)
#     else:
#         print(i,end='')
