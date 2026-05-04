a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
op=input("Enter any airthmetic operator (+,-,*,/,//,**,%): ")
if op=='+':
    print(f"Addtition of {a} and {b} is {a+b}")
elif op=='-':
    print(f"Subtraction of {a} and {b} is {a-b}")
elif op=='*':
    print(f"Mutltiplication of {a} and {b} is {a*b}")
elif op=='/':
    print(f"Division of {a} and {b} is {a/b}")
elif op=='//':
    print(f"Row division of {a} and {b} is {a//b}")
elif op=='**':
    print(f"Power  of {a} and {b} is {a**b}")
elif op=='%':
    print(f"Reminder of {a} and {b} is {a%b}")
else:
    print("Invalid output")
