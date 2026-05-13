l=[1,2,3,4,5,6,7,8,9,10]
l1=tuple(filter(lambda x:x%2==0,l))
print(f'old list: {l}')
print(f'new list: {l1}')
