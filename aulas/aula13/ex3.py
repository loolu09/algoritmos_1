#fibonacci 7 => 1 1 2 3 5 8 13

def fibonacci(y):
    if y <= 1:
        return y
    return fibonacci(y - 1) + fibonacci(y - 2)  

print("Fibonacci de 7 é: ", fibonacci(7))