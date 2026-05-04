from sys import argv as a
sum=0 
for x in a[1:]:
    sum=sum+int(x)

avg=sum/len(a[1:])
print("Average: ",avg)