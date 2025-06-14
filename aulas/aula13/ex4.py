#ex1 = inverter string: crie uma função recursiva que inverta uma string

def strinv(s):
    if len(s) == 0:
        return s
    return strinv(s[1:]) + s[0]

print(strinv('amor'))
