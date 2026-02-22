# Even Numbers from 1 to 100

even_numbers = []

for i in range(1, 101):
    if i % 2 == 0:
        even_numbers.append(i)

print("Even Numbers:", even_numbers)
print("Minimum Even Number:", min(even_numbers))
print("Maximum Even Number:", max(even_numbers))
print("Total Sum:", sum(even_numbers))



print("\nEven Numbers between 1 to 50:")
even_numbers = [i for i in range(1, 51) if i % 2 == 0]
print("List of Even Numbers:", even_numbers)
print("Three Minimum Even Numbers:", even_numbers[:3])
print("Three Maximum Even Numbers:", even_numbers[-3:])
average = sum(even_numbers) / len(even_numbers)
print("Average of Even Numbers:", average)