import random
n=int(input("Número de linhas"))
m=int(input("Número de colunas"))

a=[[0 for i in range(m)] for j in range(n)]
for j in range(n):
    for i in range(m):
        a[j][i]=random.randint(0,100)
print(a)
print()
t=a[n-1]
a[n-1]=a[0]
a[0]=t
print(a)