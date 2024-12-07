numbers = [32, 25, 456, 345, 23, 76, 89]
numbers.append(99)
numbers.insert(2, 77)
if 25 in numbers:
    numbers.remove(25)
print(numbers[:])
print(numbers[1:5])
print(numbers[5:2:-1])
print(numbers[::-1])

oddNumber = [num for num in numbers if num % 2 == 1]
print(oddNumber)