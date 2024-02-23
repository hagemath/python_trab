i = 0
incerteza = []
x = []
certo = []
while True:
    x.append(float(input('Valor X: ')))
    incerteza.append(float(input('Valor in: ')))
    i += 1
    if i == 9:
        break
for c in incerteza:
   for b in x:
       certo.append(b/(c)**2)
print(certo)