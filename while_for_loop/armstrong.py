n=int(input("Enter a number: "))
l=len(str(n))
org=n
arm=0
while n!=0:
    rem=n%10
    arm=arm+rem**l
    n=n//10
if (arm==org):
    print("Armstrong number")
else:
    print("Not Armstrong number")