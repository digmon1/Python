count = 0

for num in range(50, 201):
    original = num
    sum_power = 0
    temp = num
    digits = 0
    while temp > 0:
        temp //= 10
        digits += 1
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_power += digit ** digits
        temp //= 10
    if sum_power == num:
        print(num)
        count += 1

print("Total Armstrong numbers from 50 to 200:", count)
