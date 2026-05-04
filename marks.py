m,p,c,co,b=[int(x) for x in (input("Enter 5 subject marks of math, physcis, chemistry, computer,bio: ")).split()]
marks=(m+p+c+co+b)
average=(marks/5)
if (average>=80) and(average<100):
    print("Distinction")
elif (average>=60) and (average<70):
    print("1st division")
elif (average>=50) and (average<60):
    print("2nd division")
elif (average>=40) and (average<50):
    print("3rd division")
elif(average>=30) and (average<40):
    print("4th division")
else:
    print("Fail")