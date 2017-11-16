import random
s=1
n = int(input("Número de elementos"))
a = [0 for i in range (n)]
for i in range(n):
    a[i]=random.randint(0,1000)
    if a[i]%2 == 0:
        s*= a[i]
print(a)
if s != 1:
    print("Produto dos números pares:", s)
