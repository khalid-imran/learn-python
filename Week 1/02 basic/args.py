def totalSum(*numbers):
    sum = 0
    for num in numbers:
        sum = sum+num
    return sum
print(totalSum(1, 20, 25, 85))
