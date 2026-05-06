age=int(input("Enter the age: "))
match (age>=18):
    case 1:
        print(f"This person is eligible for vote")
    case _:
        print(f"this person is not eligible for vote")