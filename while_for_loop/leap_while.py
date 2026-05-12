a=2000
c=0
while a<3000:
    if a%400==0 or a%4==0 and a%100!=0:
        print(a)
        c=c+1
    a=a+1
print(f"The total leap year is: {c}")