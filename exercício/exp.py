
number = int(input('Digite um numero: '))
primos = []

for i in range(2, number):
    primo_i = True
    for k in range(2, i):
        if i % k == 0:
            primo_i = False
            break 
    if primo_i:
        for j in range(i + 1, number):
            primo_j = True
            for l in range(2, j):
                if j % l == 0:
                    primo_j = False
                    break  
            if primo_j and j - i == 2:
                gemeos = (i, j)
                primos.append(gemeos)

print(primos)