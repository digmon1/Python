n=int(input("Enter any two number: "))
org=n
rev=0
while n>0:
    R=n%10
    rev=rev*10+R
print("Reverse of the {n} is{rev}")