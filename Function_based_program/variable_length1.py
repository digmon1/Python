def avg(*n):
    s=0
    for i in n:
        s=s+i
    average=s/len(n)
    print(f'average is {average}')

avg(10,2,3,4)
