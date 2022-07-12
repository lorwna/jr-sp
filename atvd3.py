import json
with open("dados.json") as dadosemjson:
    dados = json.load(dadosemjson)
    
cont = 0
maior = 0
menor = 0
soma = 0
media = 0


for dia in dados:
    if (dia['valor']) != 0:
        cont = dia['valor']
        if (cont > maior):
            maior = cont
        if(menor == 0):
            menor = cont
        elif (cont < menor):
            menor = cont
        soma += dia['valor']

print("O maior valor de faturamento foi: R$ {}.".format(maior))
print('O menor valor de faturamento foi: R$ {}.'.format(menor))

media = soma / len(dados)
diasmaiores = ''

for i in dados:
    if (i['valor']) != 0:
        if (i['valor']) > media:
           diasmaiores += (str(i['dia']) + ', ')
           diasmaiores1 = diasmaiores[:-2]


print('Os dias em que o faturamento superou a média mensal de R$ {:.2f}, foram: {}.'.format(media, diasmaiores1))