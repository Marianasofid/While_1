# input

n = int(input('Digite un numero: '))

# processing
s = 0
i = 1

while i <= n:
    s = s + i
    i = i + 1

    # output

print(f"La suma de los {n} primero numeros es: {s}")