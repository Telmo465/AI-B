x=int(input("Introduza um número:"))
n=int(input("número de elementos"))
u=[0 for i in range (n)]
print(u)
for i in range(n):
    u[i]=x**(n+i)
print(u)