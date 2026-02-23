for i in range(6, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
    
    
    # Inverted Right Half Pyramid Pattern

num = 1

for i in range(1, 6):   # 5 rows
    for j in range(i):
        print(num, end=" ")
        num += 1
        if num == 10:   # Reset after 9
            num = 1
    print()