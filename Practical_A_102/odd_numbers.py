odd_numbers = []

for i in range(1, 101):
    if i % 2 != 0:
        odd_numbers.append(i)

print("Odd numbers:", odd_numbers)
print("Minimum odd number:", min(odd_numbers))
print("Maximum odd number:", max(odd_numbers))
print("Total sum:", sum(odd_numbers))