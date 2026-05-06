a=int(input("Enter any number: "))
match (a% 5==0 and a% 6==0 ):
    case True:
        print(f"{a} is exactly divisible by 5 and 6")
    case False:
        print(f"{a} is not exactly divisib;e by 5 and 6")