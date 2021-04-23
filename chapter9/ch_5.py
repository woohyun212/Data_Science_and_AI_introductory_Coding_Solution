import re

text = '''101 COM Python Part1
102 MAT LinearAlgebra
103 ENG ComputerEnglish'''
s = []
for word in text.split():
    code = re.search("^[A-Z][A-Z][A-Z]+", word)
    if code:  # None 이 아니면
        s.append(code.group())
print(s)
# 맘에 안듬 만약에 123python 의 경우에는 어떻게 처리하지?
