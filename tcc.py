# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)
Estados = ['CA','PD','PA']

TransicaoEstados = [['CACA','CAPD','CAPA'], ['PDCA','PDPD','PDPA'], ['PACA','PAPD','PAPA']]
TransicaoProbabilidades = [[0.05,0.02,0.93],[0.18,0.80,0.02],[0.05,0.02,0.93]]

listaConsumoAguaCarnista = list()
listaConsumoAguaVeg = list()
listaCenarios = list()

NumDias = 58400  #160 anos
PrevisaoHoje = Estados[0]

QtdAguaDisponivelCenarioCarnista = 9765000000000000000
QtdAguaDisponivelCenarioVeg = 9765000000000000000

Populacao = 7600000000
            
taxaAumentoPopulacao = 0.012
PessoasAumentoPorDia = 0

qtdAguaDiariaConsumidaPessoaVegetariana = 133
qtdAguaDiariaConsumidaPessoaCarnista = 4297

totalDiasCA = 0
totalDiasPD = 0
totalDiasPA = 0

def aumentarPopulacao(PopulacaoTotal):
  return PopulacaoTotal + PessoasAumentoPorDia 

def diminuirPopulacao(PopulacaoTotal):
  return PopulacaoTotal - PessoasAumentoPorDia
  
def totalPessoasPorDiaComTaxa(Populacao):
  AumentoPessoasAnual = Populacao * taxaAumentoPopulacao
  PessoasAumentoPorDia = AumentoPessoasAnual / 365
  
  return PessoasAumentoPorDia

def consumirAguaCarne(Populacao, QtdAguaDisponivel):
  return QtdAguaDisponivel - (qtdAguaDiariaConsumidaPessoaCarnista  * Populacao)
  
def consumirAguaVeg(Populacao, QtdAguaDisponivel):
  return QtdAguaDisponivel - (qtdAguaDiariaConsumidaPessoaVegetariana  * Populacao) 
   
PessoasAumentoPorDia = totalPessoasPorDiaComTaxa(Populacao) #taxa do primeiro ano

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
  

  if(i % 365 == 0):
    PessoasAumentoPorDia = totalPessoasPorDiaComTaxa(Populacao)

  QtdAguaDisponivelCenarioCarnista = consumirAguaCarne(Populacao, QtdAguaDisponivelCenarioCarnista)
  QtdAguaDisponivelCenarioVeg = consumirAguaVeg(Populacao, QtdAguaDisponivelCenarioVeg)

  listaConsumoAguaCarnista.append(QtdAguaDisponivelCenarioCarnista)
  listaConsumoAguaVeg.append(QtdAguaDisponivelCenarioVeg)
  listaCenarios.append(PrevisaoHoje)

print('Total dias CA: ', totalDiasCA)
print('Total dias PA: ', totalDiasPA)
print('Total dias PD: ', totalDiasPD)

print('Qtd Agua Disponivel Cenario Carnista: ', int(QtdAguaDisponivelCenarioCarnista))
print('Qtd Agua Disponivel Cenario Veg: ', int(QtdAguaDisponivelCenarioVeg))

print('Consumo de Agua Cenario Carnista: ', int(9765000000000000000 - QtdAguaDisponivelCenarioCarnista))
print('Consumo de Agua Cenario Veg: ', int(9765000000000000000 - QtdAguaDisponivelCenarioVeg))

print('Total populacao: ', int(Populacao))

#plt.figure()
#plt.hist(listaCenarios)
#plt.show()

plt.figure()
plt.subplot(211)
plt.plot(listaConsumoAguaCarnista)
plt.ylabel('Consumo Cenario Carnista')

plt.subplot(212)
plt.plot(listaConsumoAguaVeg)
plt.ylabel('Consumo Cenario Veg:')

plt.show()
