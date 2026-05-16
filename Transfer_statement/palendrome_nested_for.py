count = 0
for num in range(50, 201):
    temp = num
    rev = 0
    for i in range(3):
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10

        if temp == 0:
            break

    if rev == num:
        print(num)
        count=count+1

print("Total palindrome numbers =", count)
