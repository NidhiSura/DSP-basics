#LINEAR CONVOLUTION USING CIRCULAR CONVOLUTION

import math
import numpy

print('Nidhi Sura\t60001198008\n\nLinear Convolution using Circular Convolution\n')
m = int(input('Enter the size of x1\t'))
ls = int(input('Enter the size of x2\t'))

#input x1(n)
x1 = []
print('\nEnter x1(n), separated by an "enter" key')
for i in range(m):
    x1.append(int(input()))

#input x2
x2 = []
print('\nEnter x2(n), separated by an "enter" key')
for i in range(ls):
    x2.append(int(input()))

print('\nx1 = ', end='')
print(x1)
print('\nx2 = ', end='')
print(x2)

#padding 0's
#N = Ls(4) + M(4) - 1 = 7, so we add 3 zeroes to make 7'
n = ls + m - 1
for i in range(n-m):
    x1.append(0)
for i in range(n-ls):
    x2.append(0)

#x2 column arrays
colmarr = [x2]
for i in range(n-1):
    colmtemp = []
    for z in range(n):
        if z==0:
            colmtemp.append(x2[n-1])
        else:
            colmtemp.append(x2[z-1])
    x2 = colmtemp
    colmarr.append(colmtemp)
print('\nMatrix of x2 = ')
#print(colmarr)

#convert columns into rows
x2matrix = []
for i in range(n):
    row = []
    for z in range(n):
        row.append(colmarr[z][i])
    x2matrix.append(row)
#print(x2matrix)
for i in x2matrix:
    for j in i:
        print(str(j), end=' ')
    print('')

#Matrix Multiplication x1 * x2matrix
multarr = []
for p in range(n):
  val = 0
  for q in range(n):
    val += (x1[q]*x2matrix[p][q])
  multarr.append(val)
print('\nLinear Convolution using Circular Convolution: y(n)=', end = '')
print(multarr)
