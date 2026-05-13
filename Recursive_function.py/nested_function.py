def f1():
    print(f'Hello this is f1() function')
    def f2():
        print(f'Hello this is f2() function')
    f2()
f1()