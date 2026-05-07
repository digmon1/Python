l=['India', 'Nepal','Australia','England', 'Norway','Pakistan','USA']
v=['A','E','I','O','U']
l1=[x for x in l if x[0] in v]
l2=[x for x in l if x[0] not in v]

print(l1)
print(l2)
l4=[[x,len(x)] for x in l  ]
print(l4)
print(type(l4))