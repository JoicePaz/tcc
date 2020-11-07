import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)
Estados = ['CA','PD','PA']

TransicaoEstados = [['CACA','CAPD','CAPA'], ['PDCA','PDPD','PDPA'], ['PACA','PAPD','PAPA']]
MatrizTransicao = [[0.05,0.02,0.93],[0.18,0.80,0.02],[0.05,0.02,0.93]]

listaConsumo = list()
NumDias = 365
PrevisaoHoje = Estados[0]

# 7,6 bilhões de pessoas
# 9 quintilhões e setecentos e sessenta e cinco quatrilhões de litros de água potável 
# 133 litros diariamente por pessoa sem considerar a carne
# quem come carne 4297 litros diariamente de água 

for i in range(1, NumDias):
  if PrevisaoHoje == 'CA':        
    Condicao = np.random.choice(TransicaoEstados[0], replace = True, p = MatrizTransicao[0])

    if Condicao == 'CACA':
      pass
    elif Condicao == 'CAPD':
      PrevisaoHoje = 'PD'
    elif Condicao == 'CAPA':
      PrevisaoHoje = 'PA'

  elif PrevisaoHoje == 'PD':
    Condicao = np.random.choice(TransicaoEstados[1], replace = True, p = MatrizTransicao[1])

    if Condicao == 'PDPD':
      pass
    elif Condicao == 'PDCA':
      PrevisaoHoje = 'CA'
    elif Condicao == 'PDPA':
      PrevisaoHoje = 'PA'

  elif PrevisaoHoje == 'PA':
    Condicao = np.random.choice(TransicaoEstados[2], replace = True, p = MatrizTransicao[2])

    if Condicao == 'PAPA':
      pass
    elif Condicao == 'PAPD':
      PrevisaoHoje = 'PD'
    elif Condicao == 'PACA':
      PrevisaoHoje = 'PA'
  
  listaConsumo.append(PrevisaoHoje)
  print(PrevisaoHoje)

plt.plot(listaConsumo)
plt.show()
