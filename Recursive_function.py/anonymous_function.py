#Filter_function
def iseven(n):
    if n%2 ==0:
        return True
    else:
        return False
l=[1,2,3,4,5,6,7,8,9,10]
l1=list(filter(iseven,l))
print(f'old list: {l}')
print(f'new list: {l1}')