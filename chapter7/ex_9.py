def overlap(string_a, string_b):
    for i in range(len(string_b), 0, -1):
        if string_a[len(string_a) - i:] == string_b[:i]:
            return string_a.replace(string_a[len(string_a) - i:], '') + string_b
    return string_a + string_b


while 1:
    string1, string2 = input().split()
    print(overlap(string1, string2))
