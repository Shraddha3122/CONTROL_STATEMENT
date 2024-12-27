# Calculate the sum of the first 50 natural numbers using a while loop.

def sum_of_natural_numbers(N):
    total = 0
    count = 1
    while count <= N:
        total += count
        count += 1

    return total

N = 50

result = sum_of_natural_numbers(N)

print("The Sum of the First", N, "Natural Numbers is:",
      result)