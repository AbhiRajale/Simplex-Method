#Simplex Method
from prettytable import PrettyTable
#Input z
print('z = ', end='')
z = list(map(int, input().split()))
##z = [5, 2, 7]
##z = [3, 9]
##z = [5, 3]
##z = [7, 5]
##z = [3, 5]
##z = [6, 3]
##print(z)
nz = len(z)

#Input Equations
print('Enter Number of Equations: ', end='')
n = int(input())
e = []
##e = [[1, 1, 2, 22],
##[3, 2, 1, 26],
##[1, 1, 1, 18]]
##e = [[1, 4, 8],
##     [1, 2, 4]]
##e = [[1, 1, 2],
##     [5, 2, 10],
##     [3, 8, 12]]
##e = [[1, 1, 6],
##     [4, 2, 12]]
##e = [[2, 4, 25],
##     [1, 1, 13]]
##e = [[2, 2, 8],
##     [3, 3, 18]]
for _ in range(n):
  e.append(list(map(int, input().split())))
##print(e)

#Input Signs
#0: <=  |  1: >=
print('Enter Signs for Equations: ')
sign = list(map(int, input().split()))

#Display Table
def dis():
  print('B', end='  ')
  print('C', end=' ')
  print('X', end=' ')
  for j in range(nz):
    print('x' + str(j+1), end=' ')
  for j in range(n):
    print('s' + str(j+1), end=' ')
  print('R')
  for i in range(n):
    print(b[i], end=' ')
    print(c[i], end=' ')
    print(round(x[i], 2), end=' ')
    for j in range(nz):
      print(round(e[i][j], 2), end='  ')
    for j in range(n):
      print(round(s[i][j], 2), end='  ')
    print(round(r[i], 2))
  print('Delta j = ', end='')
  for i in range(nz):
    print(round(dj[i], 2), end=' ')
  print()
  print()

#First Step
b = [('s'+str(i+1)) for i in range(n)]
c = [(0 if sign[i]==0 else -9999) for i in range(n)]
x = [e[i][-1] for i in range(n)]
for i in range(n):
  del e[i][-1]
s = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
  if sign[i]==0:
    s[i][i] = 1
  else:
    s[i][i] = -1
dj = [0 for i in range(nz+n)]
for i in range(nz):
  for j in range(n):
    dj[i] += c[j]*e[j][i]
dj = [(dj[i]-z[i]) for i in range(nz)]
j = dj.index(min(dj))
##print(j)
r = [(x[i]/e[i][j] if (x[i]/e[i][j])>0 else 9999) for i in range(n)]
##print(b, c, x, dj, r)
k = r.index(min(r))
dis()

#Solving
a = [-1 for i in range(n)]
while dj[j]<0:
  m = e[k][j]
  e[k] = [e[k][i]/m for i in range(nz)]
  s[k] = [s[k][i]/m for i in range(n)]
  b[k] = 'x' + str(j+1)
  c[k] = z[j]
  x[k] = r[k]
  a[k] = j
  for i in range(n):
    if i!=k:
      m = e[i][j]
      e[i] = [(-(m * e[k][l]) + e[i][l]) for l in range(nz)]
##  for i in range(n):
##    if i!=k:
##      m = e[i][j]
      s[i] = [(-(m * s[k][l]) + s[i][l]) for l in range(n)]
      x[i] = x[i] - (x[k] * m)
  dj = [0 for i in range(nz+n)]
  for i in range(nz):
    for j in range(n):
      dj[i] += c[j]*e[j][i]
  dj = [(dj[i]-z[i]) for i in range(nz)]
  j = dj.index(min(dj))
  r = [(x[i]/e[i][j] if (e[i][j])>0 else 9999) for i in range(n)]
  dis()
  k = r.index(min(r))

#Substituting to get Solution
print()
for i in range(n):
  if c[i] == -9999:
    x[i] = 0
    continue
  x[i] *= c[i]
print('z (max) = ', end='')
print(sum(x))
