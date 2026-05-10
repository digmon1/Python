cwithouts=0
wordcount=0
s="Kathmandu is the capital city of Nepal"
l=len(s)
list=s.split()
for word in list:
    cwithouts=cwithouts+ len(word)
    wordcount =wordcount +1
print(f'Total no of word:{wordcount}')
print(f'Total no of character with s.space:{l}')
print(f'Total no of character without s.space:{cwithouts}')
print(f'Total no of space only:{l-cwithouts}')