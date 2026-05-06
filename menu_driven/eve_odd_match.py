a=int(input("Enter any number: "))
match a:
    case a if (a% 2==0):
        print(f"{a} is even number")
    case _:
        print(f"{a} is odd number")
 