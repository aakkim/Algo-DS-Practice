# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple 
# which contains every number.Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

list = input('enter number sequence: ').split(',')
tuple = tuple(list)

print(list)
print(tuple)



# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class String():
    def getString(self):
        self.s = input('enter string: ')
    def printString(self):
        print(self.s.upper())

test = String()
test.getString()
test.printString()



# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

from math import sqrt
C = 50
H = 30
def calc(D):
    D = int(D)
    return str(int(sqrt((2*C*D)/H)))

D = input('enter values comma separated: ').split(',')
D = list(map(calc,D))   # applying calc function on D and storing as a list
print(",".join(D))



# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The 
# element value in the i-th row and j-th column of the array should be i _ j.*
# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

x,y = map(int,input().split(','))
list = []

for i in range(x):
    temp = []
    for j in range(y):
        temp.append(i*j)
    list.append(temp)

print(list)