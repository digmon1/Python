from random import randint
print("Welcome to bank number generator")
print("--"*40)
s=set()
partial_acc_no='********'
for x in range(100):
    a,b,c,d,e=randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9)
    random_no=str(a)+str(b)+str(c)+str(d)+str(e)
    account_number=partial_acc_no+random_no
    s.add(account_number)
print("Bank Account Number: ")
print("--"*40)
for x in s:
    print(f'Account Number: {x}')