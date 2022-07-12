n1 = 0
n2 = 1
contador = 0
soma = 0
fibonacci = [0, 1]
limite = 15 #Número definido por preferências estéticas.
numero = int(input('Digite um número para saber se ele está presente na sequêcia de Fibonacci até o número que foi delimitada: '))

while contador < limite:
    soma = n1 + n2
    fibonacci.append(soma)
    n1 = n2
    n2 = soma
    contador += 1
    
print("=" *21, "SEQUÊNCIA DE FIBONACCI", "=" *21)
print(fibonacci)
print("=" *66)

if numero in fibonacci:
    print("O número {} está presente na sequência de Fibonacci.".format(numero))
else:
    print("O número {} não está presente na sequência de Fibonacci.".format(numero))
    