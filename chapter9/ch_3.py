import random

n_digits = int(input("몇 자리의 비밀번호를 원하십니까?"))

otp = ''
for i in range(n_digits):
    r = random.randint(0, 2)
    if r == 0:
        otp += chr(random.randint(48, 57))
    if r == 1:
        otp += chr(random.randint(65, 90))
    if r == 2:
        otp += chr(random.randint(97, 122))
print(otp)
