#OVERLAP SAVE METHOD

print('Nidhi Sura\t60001198008\n\nOverlap Save Method\n')

#Taking inputs
n = int(input('\nEnter the no. of terms in x(n)\t'))
x = []
print('\nEnter the terms of x(n), separated by an "enter"')
for _ in range(n):
    x.append(int(input()))

m = int(input('\nEnter the no. of terms in h(n)\t'))
h = []
print('\nEnter the terms of h(n), separated by an "enter"')
for _ in range(m):
    h.append(int(input()))

ls = input('\nEnter the value of Ls, if nothing is entered, default = 5\t')
if ls == '':
    ls = 5
ls = int(ls)

print('\nx(n) = ', end='')
print(x)
print('\nh(n) = ', end='')
print(h)
print('ls = ' + str(ls))

#padding 0's in h(n)
for _ in range(ls-m):
    h.append(0)

#Arrays x1, x2, x3...
xarrays = []
arrtemp = []
for _ in range(m-1):
    arrtemp.append(0)
for i in range(ls-(m-1)):
    arrtemp.append(x[i])
xarrays.append(arrtemp)
length = ls-2*(m-1)
x = x[length:]

while(len(x)>ls):
    arrtemp = []
    for i in range(ls):
        arrtemp.append(x[i])
    xarrays.append(arrtemp)
    x = x[ls-(m-1):]

arrtemp = []
for i in x:
    arrtemp.append(i)
if len(arrtemp)!=ls:
    for _ in range(ls-len(arrtemp)):
        arrtemp.append(0)
xarrays.append(arrtemp)
print('Valaues of x1, x2, x3 arrays =')
print(xarrays)

#creating the h matrix
#h(x) column arrays
colmarr = [h]
for _ in range(ls-1):
    colmtemp = []
    for z in range(ls):
        if z==0:
            colmtemp.append(h[ls-1])
        else:
            colmtemp.append(h[z-1])
    h = colmtemp
    colmarr.append(colmtemp)

#convert columns into rows
hmatrix = []
for i in range(ls):
    row = []
    for z in range(ls):
        row.append(colmarr[z][i])
    hmatrix.append(row)

print('Matrix of h(x) = ')
for i in hmatrix:
    for j in i:
        print(str(j), end=' ')
    print('')

#now calculating the y arrays
yarrays = []
for arrtemp in xarrays:
    yn = []
    for p in range(ls):
      val = 0
      for q in range(ls):
        val += (arrtemp[q]*hmatrix[p][q])
      yn.append(val)
    yarrays.append(yn)

print('yarrays = ')
print(yarrays)

finalyn = []
for i in yarrays:
    for j in i[m-1:]:
        finalyn.append(j)
print('\nValue of y(n) = ', end='')
print(finalyn)
