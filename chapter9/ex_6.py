import re

s = 'English = 89, Science = 90, Math = 92, History = 80'

print('문장 s :', s)
total = 0
for i in re.findall('\d+', s):
    total += int(i)
print('총점 :', total)
print('평균 :', total / len(re.findall('\d+', s)))
