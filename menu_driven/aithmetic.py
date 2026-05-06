print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor division")
print("6. Exponential/power")
print("7. Remainder/Mode")
ch =int(input("Enter your choice...."))
match ch:
    case 1:
        a=int(input("Enter 1st number: "))
        b=int(input("Enter 2nd number: "))
        print(f"Addition of {a} and {b} is {a+b}")
    case 2:
        a=int(input("Enter 1st number: "))
        b=int(input("Enter 2nd number: "))
        print(f"Subtraction of {a} and {b} is {a-b}")
    case 3:
        a=int(input("Enter 1st number: "))
        b=int(input("Enter 2nd number: "))
        print(f"Multiplication of {a} and {b} is {a*b}")
    case 4:
        a=int(input("Enter 1st number: "))
        b=int(input("Enter 2nd number: "))
        print(f"Division of {a} and {b} is {a/b}")
    case 5:
        a=int(input("Enter 1st number: "))
        b=int(input("Enter 2nd number: "))
        print(f"Floor division of {a} and {b} is {a//b}")
    case 6:
        a=int(input("Enter 1st number: "))
        b=int(input("Enter 2nd number: "))
        print(f"Power of {a} by {b} is {a**b}")
    case 7:
        a=int(input("Enter 1st number: "))
        b=int(input("Enter 2nd number: "))
        print(f"Remainder of {a} and {b} is {a%b}")
    case _:
        print("Invalid choice.... Please enter from [1-7]")
    
    