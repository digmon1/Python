n=int(input("Enter any  +ve number: "))
print(f"Fibonacci series of number {n}")
first=0
second=1
print(first)
print(second)

i=3
while i<=n:
    third=first+second
    print(third)
    first=second
    second=third
    i=i+1