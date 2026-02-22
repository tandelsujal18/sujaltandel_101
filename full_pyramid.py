# Full Pyramid (Reverse)

rows = 5

for i in range(1, rows + 1):
    # Print leading spaces
    for space in range(rows - i):
        print(" ", end="")

    # Print alphabets
    for j in range(i):
        print(chr(65 + j), end=" ")

    print()
    
    
rows = 5

for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print()
    


