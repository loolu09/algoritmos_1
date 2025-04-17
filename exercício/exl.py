
number = int(input('Digite um número: '))

for i in range(number, 0, -1):
    print(end=" ")
    for j in range(1, i + 1):
        print(j, end = ' ')
    print(" ")