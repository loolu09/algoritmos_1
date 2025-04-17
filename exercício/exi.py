
frase = input('Digite uma frase: ').lower()
quantidade_vogais = 0
vogais = 'aeiou'

for letra in frase:
    if letra in vogais:
        quantidade_vogais += 1
print(f'A quantidade de vogais na frase: {frase}, é {quantidade_vogais}')