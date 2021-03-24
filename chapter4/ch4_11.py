s_id = 'ilovepython'
s_pswd = 'mypass1234'
id = input("아이디를 입력하시오 : ")
if s_id == id:
    pswd = input("비밀번호를 입력하시오 : ")
    if s_pswd == pswd:
        print("환영합니다.")
    else:
        print("비밀번호가 다릅니다.")
else:
    print("아이디를 찾을 수 없습니다.")