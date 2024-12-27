# Write a program to calculate the power of a number without using the operator.


base = int(input('Enter base value: '))
exponent = int(input('ENter exponent value: '))

ans = 1
for i in range(exponent):
    ans *=  base

print(f'Answer is : {ans}')