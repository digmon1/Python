c=0
for n in range (50,1000):
    l=len(str(n))
    org=n
    arm=0
    while n!=0:
        rem=n%10
        arm=arm+rem**1
        n=n//10
    if(arm==org):
        print(org)
        c=c+1
print(f"total no of armstron is {c}")