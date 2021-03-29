i, j = 1, 1

while j <= 9:
    while i <= 9:
        print("%s * %s = %-10s" % (i, j, i * j), end=" ")
        i += 1
    print()
    j += 1
    i = 1
