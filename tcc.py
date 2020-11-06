import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)
Estados = ['CA','PD','PA']

TransicaoEstados = [['CACA','CAPD','CAPA'], ['PDCA','PDPD','PDPA'], ['PACA','PAPD','PAPA']]
MatrizTransicao = [[0.05,0.02,0.93],[0.18,0.80,0.02],[0.05,0.02,0.93]]

listaConsumo = list()
NumDias = 365
PrevisaoHoje = Estados[0]

for i in range(1, NumDias):
  if PrevisaoHoje == 'CA':        
    Condicao = np.random.choice(TransicaoEstados[0], replace = True, p = MatrizTransicao[0])

    if Condicao == 'CAPA':
      pass
    else:
      PrevisaoHoje = 'PD'

  elif PrevisaoHoje == 'PD':
    Condicao = np.random.choice(TransicaoEstados[1], replace = True, p = MatrizTransicao[1])

    if Condicao == 'CAPD':
      pass
    else:
      PrevisaoHoje = 'PA'
  
  listaConsumo.append(PrevisaoHoje)
  print(PrevisaoHoje)

plt.plot(listaConsumo)
plt.show()
