import re

sent = input("문장을 입력하시오 : ")
# sent = 'Jian777 is very famous Data scientist. He is only 26 years old but published 19 papers.'
eng_word, num_word, epn_word = [], [], []

for i in sent.split():
    i = i.replace('.', '')
    if re.search('^[a-zA-Z]*$', i) is not None:
        eng_word.append(i)
    elif re.search('^\d*$', i) is not None:
        num_word.append(i)
    else:
        epn_word.append(i)
print('영문 단어 : ' + ' '.join(eng_word))
print('숫자 : ' + ' '.join(num_word))
print('영문자+숫자 : ' + ' '.join(epn_word))
