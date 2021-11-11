import math
import numpy

n = int(input('Enter the size of the vector'))

#input x1(n)
x1 = []
print('Enter x1(n), separated by an "enter" key')
for i in range(n):
    x1.append(int(input()))

#input x2
x2 = []
print('Enter x2(n), separated by an "enter" key')
for i in range(n):
    x2.append(int(input()))

#CIRCULAR CONVOLUTION

#twiddle matrix 1
j = 0 + 1j
arrfin = []

for p in range(n):
  arrtemp = []
  for q in range(n):
    val = (math.e)**((-j*2*math.pi*p*q)/n)
    arrtemp.append(val)
  arrfin.append(arrtemp)
arrfin = numpy.round(arrfin)

#DFT
X1k = []
for p in range(n):
  val = 0
  for q in range(n):
    val += x1[q]*arrfin[p][q]
  X1k.append(val)

X2k = []
for p in range(n):
  val = 0
  for q in range(n):
    val += x2[q]*arrfin[p][q]
  X2k.append(val)
#print(X1k,X2k)

#Multiplication
Yck = []
for i in range(n):
    Yck.append(X1k[i]*X2k[i])
#print(Yck)

#twiddle matrix 2
arrfin2 = []

for p in range(n):
  arrtemp = []
  for q in range(n):
    val = (math.e)**((j*2*math.pi*p*q)/n)
    arrtemp.append(val)
  arrfin2.append(arrtemp)
arrfin2 = numpy.round(arrfin2)

#IDFT
ycn = []
for p in range(n):
  val = 0
  for q in range(n):
    val += (Yck[q]*arrfin2[p][q])/n
  ycn.append(val)
print('Circular Convolution: yc(n)=', end = '')
print(ycn)

#LINEAR CONVOLUTION USING CIRCULAR CONVOLUTION

#padding 0's
#N = Ls(4) + M(4) - 1 = 7, so we add 3 zeroes to make 7'
for i in range(n-1):
    x1.append(0)
    x2.append(0)

#x2 column arrays
colmarr = [x2]
for i in range(2*n-2):
    colmtemp = []
    for z in range(2*n-1):
        if z==0:
            colmtemp.append(x2[2*n-2])
        else:
            colmtemp.append(x2[z-1])
    x2 = colmtemp
    colmarr.append(colmtemp)
#print(colmarr)

#convert columns into rows
x2matrix = []
for i in range(2*n-1):
    row = []
    for z in range(2*n-1):
        row.append(colmarr[z][i])
    x2matrix.append(row)
print(x2matrix)

#Matrix Multiplication x1 * x2matrix
multarr = []
for p in range(2*n-1):
  val = 0
  for q in range(2*n-1):
    val += (x1[q]*x2matrix[p][q])
  multarr.append(val)
print('Linear Convolution using Circular Convolution: y(n)=', end = '')
print(multarr)

#LINEAR CONVOLUTION

#padding 0's already done, code is too chaotic, arrange later

#twiddle matrix 1
j = 0 + 1j
arrfin = []

for p in range(2*n-1):
  arrtemp = []
  for q in range(n):
    val = (math.e)**((-j*2*math.pi*p*q)/n)
    arrtemp.append(val)
  arrfin.append(arrtemp)
arrfin = numpy.round(arrfin)
    val += x1[q]*arrfin[p][q]

#twiddle matrix 2
arrfin2 = []

for p in range(2*n-1):
  arrtemp = []
  for q in range(n):
    val = (math.e)**((j*2*math.pi*p*q)/n)
    arrtemp.append(val)
  arrfin2.append(arrtemp)
arrfin2 = numpy.round(arrfin2)

#DFT
X1k = []
for p in range(2*n-1):
  val = 0
  for q in range(2*n-1):
    val += x1[q]*arrfin[p][q]
  X1k.append(val)

X2k = []
for p in range(2*n-1):
  val = 0
  for q in range(2*n-1):
    val += x2[q]*arrfin[p][q]
  X2k.append(val)
#print(X1k,X2k)

#Multiplication
Yck = []
for i in range(2*n-1):
    Yck.append(X1k[i]*X2k[i])
#print(Yck)

#IDFT
ycn = []
for p in range(2*n-1):
  val = 0
  for q in range(2*n-1):
    val += (Yck[q]*arrfin2[p][q])/n
  ycn.append(val)
print('Linear Convolution: yc(n)=', end = '')
print(ycn)
