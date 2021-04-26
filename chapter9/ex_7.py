import string

sent = list(input("문장을 입력하시오 : "))
moving_index = int(input("이동시킬 칸 수를 입력하시오 : "))
asciis = string.ascii_lowercase + string.ascii_uppercase
for i in list(sent):
    if i in asciis:
        sent[sent.index(i)] = asciis[(asciis.index(i) + moving_index) % len(asciis)]
# moving_index 가 1일 때, Z가 입력되면 a가 출력되도록 하였다.
print("암호화된 문장 : " + ''.join(sent))
