a,b=[int (x) for x in(input("enter any two number: ")).split()]
match a,b:
    case a,b if (a>b):
        print(f"{a} is greater than {b}")
    case _:
        print(f"{a} is less than {b}")