# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between
# 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

import math
for x in range(2000, 3201):
    if (x % 7 == 0) and (x % 5 != 0):
        print(x, end=',')

# OR

list = []
for x in range(2000, 3201):
    if (x % 7 == 0) and (x % 5 != 0):
        list.append(x)
print(list, sep=',')


# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated
# sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320


def factOfNum(x):
    if x == 0:
        return 1
    else:
        return math.factorial(x)


print(factOfNum(8))

# OR


def factOfNum2(n):
    fNum = 1
    for x in range(1, n+1):
        fNum = fNum * x
    return fNum


print(factOfNum2(8))


# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number
# between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

number = int(input('enter number: '))
dictionary = {}
for num in range(1, number+1):
    dictionary[num] = num * num
print(dictionary)
