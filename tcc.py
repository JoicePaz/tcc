import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)
Estados = ['CA','PD','PA']

TransicaoEstados = [['CACA','CAPD','CAPA'], ['PDCA','PDPD','PDPA'], ['PACA','PAPD','PAPA']]
TransicaoProbabilidades = [[0.05,0.02,0.93],[0.18,0.80,0.02],[0.05,0.02,0.93]]

listaConsumoAguaCarnista = list()
listaConsumoAguaVeg = list()

NumDias = 58400
PrevisaoHoje = Estados[0]

QtdAguaDisponivelCenarioCarnista = 9765000000000000000
QtdAguaDisponivelCenarioVeg = 9765000000000000000

Populacao = 7600000000
taxaAumentoPopulacao = 0.012

qtdAguaDiariaConsumidaPessoaVegetariana = 133
qtdAguaDiariaConsumidaPessoaCarnista = 4297

totalDiasCA = 0
totalDiasPD = 0
totalDiasPA = 0

def aumentarPopulacao(Populacao):
  AumentoPessoasAnual = Populacao * taxaAumentoPopulacao
  PessoasAumentoPorDia = int(AumentoPessoasAnual / NumDias)
  NovaPopulacao = PessoasAumentoPorDia + Populacao
  
  return NovaPopulacao

def diminuirPopulacao(Populacao):
  AumentoPessoasAnual = Populacao * taxaAumentoPopulacao
  PessoasAumentoPorDia = int(AumentoPessoasAnual / NumDias)
  NovaPopulacao = PessoasAumentoPorDia - Populacao
  
  return NovaPopulacao

def consumirAguaCarne(Populacao, QtdAguaDisponivel):
  return QtdAguaDisponivel - (qtdAguaDiariaConsumidaPessoaCarnista  * Populacao)
  
def consumirAguaVeg(Populacao, QtdAguaDisponivel):
  return QtdAguaDisponivel - (qtdAguaDiariaConsumidaPessoaVegetariana  * Populacao)
  
for i in range(1, NumDias):
  if PrevisaoHoje == 'CA':        
    Condicao = np.random.choice(TransicaoEstados[0], replace = True, p = TransicaoProbabilidades[0])

    if Condicao == 'CACA':
      totalDiasCA += 1
    elif Condicao == 'CAPD':
      PrevisaoHoje = 'PD'
      totalDiasPD += 1
      Populacao = diminuirPopulacao(Populacao)
    elif Condicao == 'CAPA':
      PrevisaoHoje = 'PA'
      totalDiasPA += 1
      Populacao = aumentarPopulacao(Populacao)

  elif PrevisaoHoje == 'PD':
    Condicao = np.random.choice(TransicaoEstados[1], replace = True, p = TransicaoProbabilidades[1])

    if Condicao == 'PDPD':
      totalDiasPD += 1
      Populacao = diminuirPopulacao(Populacao)
    elif Condicao == 'PDCA':
      PrevisaoHoje = 'CA'
      totalDiasCA += 1
    elif Condicao == 'PDPA':
      PrevisaoHoje = 'PA'
      totalDiasPA += 1
      Populacao = aumentarPopulacao(Populacao)

  elif PrevisaoHoje == 'PA':
    Condicao = np.random.choice(TransicaoEstados[2], replace = True, p = TransicaoProbabilidades[2])

    if Condicao == 'PAPA':
      totalDiasPA += 1
      Populacao = aumentarPopulacao(Populacao)
    elif Condicao == 'PAPD':
      PrevisaoHoje = 'PD'
      totalDiasPD += 1
      Populacao = diminuirPopulacao(Populacao)
    elif Condicao == 'PACA':
      PrevisaoHoje = 'CA'
      totalDiasCA += 1
  
  QtdAguaDisponivelCenarioCarnista = consumirAguaCarne(Populacao, QtdAguaDisponivelCenarioCarnista)
  QtdAguaDisponivelCenarioVeg = consumirAguaVeg(Populacao, QtdAguaDisponivelCenarioVeg)

  listaConsumoAguaCarnista.append(QtdAguaDisponivelCenarioCarnista)
  listaConsumoAguaVeg.append(QtdAguaDisponivelCenarioVeg)

  # listaConsumo.append(PrevisaoHoje)

print('Total dias CA: ', totalDiasCA)
print('Total dias PA: ', totalDiasPA)
print('Total dias PD: ', totalDiasPD)

plt.plot(listaConsumoAguaCarnista)
plt.show()

plt.plot(listaConsumoAguaVeg)
plt.show()
