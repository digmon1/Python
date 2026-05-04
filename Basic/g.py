n = int(input("Enter any number: "))
org = n
sum_digits = 0

for digit in str(n):
    sum_digits += int(digit)

print(f"Sum of the digits of {org} is {sum_digits}")