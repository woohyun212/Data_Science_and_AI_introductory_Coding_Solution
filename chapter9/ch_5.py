import re

text = '''101 COM 123Python Part1
102 MAT LinearAlgebra
103 ENG ComputerEnglish'''
s = []
for word in text.split():
    code = re.search("^\d*$", word)
    if code:  # None 이 아니면
        s.append(code.group())
print(s)

