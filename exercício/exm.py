
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
mdc = 1

if n1 < n2:
    a = n1
else:
    a = n2

for i in range(1, a):
    if n1 % i == 0 and n2 % i == 0:
        mdc = i
print(mdc)