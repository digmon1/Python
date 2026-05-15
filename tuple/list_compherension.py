l=[1,2,3,4,5,6,7,8,9]
l1=(x for x in l if x%2==0)
print(f'old tuple:{l}')
print(f'new tuplee:{l1}')
l2=(x**2 for x in l)
print(f'square list:{l2}')