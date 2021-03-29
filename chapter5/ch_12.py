string = list(input("단어를 입력하세요 : "))
vowel = ['a', 'e', 'i', 'o', 'u']
for i in string:
    if i in vowel:
        break
    print(i, end="")
