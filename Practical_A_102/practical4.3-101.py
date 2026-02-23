# Odd numbers between 1 to 50
odd_numbers = [x for x in range(1, 51) if x % 2 != 0]
print("Odd numbers:", odd_numbers)

# Minimum 3 odd numbers
min_three = sorted(odd_numbers)[:3]
print("Three minimum odd numbers:", min_three)

# Maximum 3 odd numbers
max_three = sorted(odd_numbers)[-3:]
print("Three maximum odd numbers:", max_three)

# Average of odd numbers
average = sum(odd_numbers) / len(odd_numbers)
print("Average of odd numbers:", average)