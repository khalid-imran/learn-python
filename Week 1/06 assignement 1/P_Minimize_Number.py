'''
Given a number N and an array A of N positive numbers. Print maximum possible operations that can be performed.

The operation is as follows: if all numbers are even then divide each of them by 2 otherwise, you can not perform any more operations.

Input
First line contains a number N (1 ≤ N ≤ 200) number of elements.

Second line contains N numbers (1  ≤  Ai  ≤  109).

Output
Print the maximum possible number of operations that can be performed.
'''


val = int(input())
int_lsit = list(map(int, input().split()))
c = 0
while all(i % 2 == 0 for i in int_lsit):
    int_lsit = [i / 2 for i in int_lsit]
    c = c + 1
print(c)
