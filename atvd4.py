sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
total = sp + rj + mg + es + outros
psp = (100 * 67836.43) / total
prj = (100 * 36678.66) / total
pmg = (100 * 29229.88) / total
pes = (100 * 27165.48) / total
poutros = (100 * 19849.53) / total
porcetagemtotal = psp + prj + pmg + pes + poutros
print("O valor total mensal da distribuidora é: R$ {}.\nCom R$ {}, São Paulo teve o percentual de: {:0.2f}%.".format(total, sp, psp))
print("Com R$ {}, Rio de Janeiro teve o percentual de: {:0.2f}%.\nCom R$ {}, Minas Gerais teve o percentual de: {:0.2f}%.".format(rj, prj, mg, pmg))
print("Com R$ {}, Espirito Santo teve o percentual de: {:0.2f}%.\nCom R$ {}, outros estados tiveram o percentual de: {:0.2f}%.".format(es, pes, outros, poutros))
print("Totalizando assim os {}% do rendimento mensal.".format(porcetagemtotal))