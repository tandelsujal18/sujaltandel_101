rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)
    
    
    # Full Pyramid Alphabet Pattern

rows = 5

for i in range(rows):
    # Print spaces
    print(" " * i, end="")
    
    # Print alphabets
    for j in range(rows - i):
        print(chr(65 + j), end=" ")
    
    print()