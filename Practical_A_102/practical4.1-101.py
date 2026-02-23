# Inverted Right Half Pyramid Pattern
num = 1
rows = 5
for i in range(1, rows+1):
    for j in range(i):
        print(num, end=' ')
        num += 1
        if num > 9:
            num = 1
    print()