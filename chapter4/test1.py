def func1_true():
    print("func1 실행됨")
    return True


def func2_false():
    print("func2 실행됨")
    return False


def blabla():
    print("블라블라")
    return


if func2_false() and func1_true():
    blabla()

print("-----------------")
if all([func2_false(), func1_true(), func2_false(), func2_false(), func2_false(), func2_false(),]):
    blabla()
