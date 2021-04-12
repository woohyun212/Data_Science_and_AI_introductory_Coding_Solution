code = ('A', 'B', 'C')
num = ('1', '2')
seat = []
for i in code:
    for j in num:
        seat.append(f'{i}{j}')
print(seat)
