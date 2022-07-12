frase = str(input("Digite uma string para ser invertida")).upper()
separar = frase.split()
juntar = ''.join(separar)
inverso = ''
invertido = ''
tamanho =len(juntar)
for letra in range(tamanho - 1, -1, -1):
    inverso += juntar[letra]
for letra1 in range(len(frase) - 1, -1, -1):
    invertido += frase[letra1]
    
print("A frase digitada foi: {}.\nInvertida sem espaços fica: {}.\nInvertida com espaços fica:{}.".format(frase,inverso, invertido))