m,p,c,co,b=[int(x) for x in (input("Enter 5 subject marks of math, physcis, chemistry, computer,bio: ")).split()]
marks=(m+p+c+co+b)
average=(marks/5)
match average:
    case average if (average>=90) and(average<100):
        print("Grade is Disctinction")
    case average if (average>=85) and (average<90):
        print("Grade is A+")
    case average if (average>=80) and (average<85):
        print("Grade is A")
    case average if (average>=75) and (average<80):
        print("Grade is B+")
    case average if(average>=70) and (average<75):
        print("Grade is B")
    case average if(average>=65) and (average<70):
        print("Grade is C+")
    case average if(average>=60) and (average<65):
        print("Grade is C")
    case average if(average>=55) and (average<60):
     print("Grade is D+")
    case average if(average>=50) and (average<55):
        print("Grade is D")
    case _:
        print("Fail")