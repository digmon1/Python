m,p,c,co,b=[int(x) for x in (input("Enter 5 subject marks of math, physcis, chemistry, computer,bio: ")).split()]
marks=(m+p+c+co+b)
average=(marks/5)
match average:
    case average if (average>=80) and(average<100):
        print("Distinction")
    case average if (average>=60) and (average<70):
        print("1st division")
    case average if (average>=50) and (average<60):
        print("2nd division")
    case average if  (average>=40) and (average<50):
        print("3rd division")
    case average if(average>=30) and (average<40):
        print("4th division")
    case _:
        print("Fail")