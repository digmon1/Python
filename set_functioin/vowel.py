s1=set()
s='missippiiese'
v={'a','e','i','o','u'}
for x in s:
    if x.lower() in v:
        s1.add(x.lower())
print(f'set of uniique vowel: {s1}')   