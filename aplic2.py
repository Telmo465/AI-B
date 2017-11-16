n=int(input("Número de terrenos"))
a=0
for i in range(n):
    h=float(input("Altura:"))
    b=float(input("Base menor:"))
    B=float(input("Base maior:"))
    a += (B+b)/2*h
print("Área total:", a, "m2")