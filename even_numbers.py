# Even Numbers from 1 to 100

even_numbers = []

for i in range(1, 101):
    if i % 2 == 0:
        even_numbers.append(i)

print("Even Numbers:", even_numbers)
print("Minimum Even Number:", min(even_numbers))
print("Maximum Even Number:", max(even_numbers))
print("Total Sum:", sum(even_numbers))