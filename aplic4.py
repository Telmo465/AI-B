n = int(input("Introduza um número"))
t=0
for x in range(1, n+1):
    if n%x == 0:
        t+=1
print("O número", n, "tem", t, "divisores")