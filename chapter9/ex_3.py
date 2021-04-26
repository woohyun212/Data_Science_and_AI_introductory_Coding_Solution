import re

string = input('문자열을 입력하시오 : ')

print("대문자, 소문자, 숫자, 특수문자의 개수")
print('대문자 =', len(re.findall("[A-z]", string)))
print('소문자 =', len(re.findall("[a-z]", string)))
print('숫자 =', len(re.findall('\d', string)))
print('특수문자 =', len(re.findall('\W', string)))
