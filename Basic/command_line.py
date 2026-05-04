import sys
print(type(sys.argv))
print(sys.argv[1:])
for x in sys.argv[1:]:
    print(x)