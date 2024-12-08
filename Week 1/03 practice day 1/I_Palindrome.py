# Given a number N
# . Print 2 lines that contain the following respectively:

# Print N
#  in a reversed order and not leading zeroes.
# If N
#  is a palindrome number print "YES" otherwise, print "NO.
# Note:

# A palindrome number is a number that reads the same forward or backward.

# For example: 12321, 101 are palindrome numbers, while 1201, 221 are not.

# A leading zero is any 0 digit that comes before the first nonzero digit in a number for example : numbers (005 , 01 , 0123 , 02 , 000250 )
# are leading zeroes but ( 5 , 123 , 20 ,2500 ) not leading zeroes numbers .
i = input()
reverse = i[::-1]
reverse = reverse.lstrip('0')
if i == reverse:
    print(reverse)
    print('YES')
else:
    print(reverse)
    print('NO')
