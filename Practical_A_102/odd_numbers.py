odd_numbers = []

for i in range(1, 101):
    if i % 2 != 0:
        odd_numbers.append(i)

print("Odd numbers:", odd_numbers)
print("Minimum odd number:", min(odd_numbers))
print("Maximum odd number:", max(odd_numbers))
print("Total sum:", sum(odd_numbers))


# Odd numbers between 1 and 50

odd_numbers = []

for i in range(1, 51):
    if i % 2 != 0:
        odd_numbers.append(i)

print("Odd Numbers:", odd_numbers)

# Three minimum odd numbers
print("Three Minimum Odd Numbers:", odd_numbers[:3])

# Three maximum odd numbers
print("Three Maximum Odd Numbers:", odd_numbers[-3:])

# Average of odd numbers
average = sum(odd_numbers) / len(odd_numbers)
print("Average of Odd Numbers:", average)