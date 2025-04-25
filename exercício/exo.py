
n = int(input('Digite um número: '))
a, b = 0, 1 
fibonacci = []

for i in range(n, 0, -1): #?? pq nao ficou decrescente?
    a, b = 1, 0
    for j in range(i):
        a, b = b, a + b
    print(a, end=' ')
