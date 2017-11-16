import random
n=int(input("Número de linhas"))
m=int(input("Número de colunas"))
v=[]
t=0
a=[[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j]=random.randint(0,10)
for i in range(len(a)):
    s=1
    for j in range(len(a[0])):
        if(a[i][j] %2) != 0:
            s*=a[i][j]            
    if s==1:
        v.append(0)
    else:
        v.append(s)
for x in range(len(v)):
    t+=v[x]
print(a)
print(v)
print(t)