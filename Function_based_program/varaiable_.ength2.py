def avg(**n):
    s=0
    for i,j in n.items():
        s=s+j
    average=s/len(n)
    print(f'average is {average}')

avg(a=1,b=2,c=3)
