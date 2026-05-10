status=0
s="Lbef is the it college of Nepal"
ch=input("enter any character:")
pos=-1
while True:
    pos=s.find(ch,pos+1,len(s)-1)
    if pos==-1:
        break
    print (f'{ch} occurs of index {pos}')
    status=1
if status==0:
    print(f' {ch} is not available in the status')