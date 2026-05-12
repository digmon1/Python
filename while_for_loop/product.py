n = int(input("Enter any number: "))
org = n
product = 1

while n != 0:
    R = n % 10
    product = product * R
    n = n // 10

print(f"The product of the digits of {org} is {product}")