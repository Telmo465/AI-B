import random

n = random.randint(0,11)
t=1
x=int(input("DIgite um número entre 0 e 10:"))
while x != n:
    t+=1
    if x > n:
        print("Tente um número menor!")
    elif x < n:
        print("Tente um número maior!")
    x=int(input("DIgite um número entre 0 e 10:"))
print("Acertou!!")
print("Número de tentativas:", t)
    