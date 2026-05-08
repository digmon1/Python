l=[1,2,3,4,5]
s={x**2 for x in l}
print(s)
s1={x**2 for x in l if x%2!=0}
print(s1)