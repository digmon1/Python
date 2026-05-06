year=int(input("Enter year: "))
match year:
    case year if (year% 400==0 or year%  4==0 and year% 100!=0):
        print(year,"is a leap year")
    case _:
        print(year,"is not a leap year")
