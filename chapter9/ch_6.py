import re

txt = 'abc@facebook.com와 bbc@google.com에서 이메일이 도착하였습니다.'

email = re.findall('\S+@[a-zA-z]+',txt)
for i in email:
    id, domain = i.split('@')
    print(f"추출된 아이디 : {id}, 도메인 : {domain}")