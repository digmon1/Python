ch=input("enter any character: ")
if ch .isalnum():
    print(f"{ch} is an alphanumeric")
    if ch .isalpha():
        print(f"{ch} is an alphabet")
        if ch.lower():
            print(f"{ch} is in lowercase")
        else:
            print(f"{ch} in uppercase")
    else:
        print(f"{ch} is a digit")
elif ch .isspace():
    print(f"{ch} is a space only")
else:
    print(f"{ch} is an special character")