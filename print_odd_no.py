# Print only odd numbers from a list using the continue statement.

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for num in numbers:
    if num % 2 == 0:
        continue
    print(f"Odd number: {num}")
