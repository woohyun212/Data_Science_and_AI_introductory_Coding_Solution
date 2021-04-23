t = "It's Not The RIght Time To Conduct Exams. MY DEMAND IN BOLD AND CAPITAL." \
    " NO EXAMS IN COVID!!!"
capital_count = 0
exclamation_mark_C = 0
for i in list(t):
    if str(i).isupper():
        capital_count += 1
    elif str(i)=="!":
        exclamation_mark_C +=1
print("느낌표 개수:", exclamation_mark_C)
print("대문자 개수:", capital_count)
