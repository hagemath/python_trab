i = 0
incerteza = []
while True:
    incerteza.append(float(input('Valor: ')))
    i += 1
    if i == 9:
        break
certo=[]
for c in incerteza:
    certo.append(1/c**2)
print(certo)
a = sum(certo)
print(a)
