count=0
for x in range (50,201):
    for i in range (2,x):
        if x %i==0:
            break
    else:
        print(x)
        count +=1
print("The total prime number=", count)