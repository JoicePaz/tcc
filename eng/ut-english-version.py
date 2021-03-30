# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)
States = ['CA','PD','PA']

TransitionStates = [['CACA','CAPD','CAPA'], ['PDCA','PDPD','PDPA'], ['PACA','PAPD','PAPA']]
TransitionProbabilities = [[0.05,0.02,0.93],[0.18,0.80,0.02],[0.05,0.02,0.93]]

consumptionWaterCarnistList = list()
consumptionWaterVeg = list()
scenariosList = list()

NumDays = 58400  #160 anos
TodayState = States[0]

QuantityWaterAvailableCarnist = 9765000000000000000
QuantityWaterAvailableVeg = 9765000000000000000

Population = 7600000000
            
PopulationGrowthTax = 0.012
PeopleIncreaseByDay = 0

quantityDailyWaterConsumedVeg = 133
quantityDailyWaterConsumedCarnist = 4297

totalDaysCA = 0
totalDaysPD = 0
totalDaysPA = 0

def populationIncrease(PopulationTotal):
  return PopulationTotal + PeopleIncreaseByDay 

def populationDecrease(PopulationTotal):
  return PopulationTotal - PeopleIncreaseByDay
  
def totalPeopleByDayWithRate(Population):
  IncreasePeopleAnnual = Population * PopulationGrowthTax
  PeopleIncreaseByDay = IncreasePeopleAnnual / 365
  
  return PeopleIncreaseByDay

def waterConsumptionCarnist(Population, quantityWaterAvailable):
  return quantityWaterAvailable - (quantityDailyWaterConsumedCarnist * Population)
  
def waterConsumptionVeg(Population, quantityWaterAvailable):
  return quantityWaterAvailable - (quantityDailyWaterConsumedVeg  * Population) 
   
PeopleIncreaseByDay = totalPeopleByDayWithRate(Population) #first year rate

for i in range(NumDays):
  if TodayState == 'CA':        
    Condition = np.random.choice(TransitionStates[0], replace = True, p = TransitionProbabilities[0])

    if Condition == 'CACA':
      totalDaysCA += 1
    elif Condition == 'CAPD':
      TodayState = 'PD'
      totalDaysPD += 1
      Population = populationDecrease(Population)
    elif Condition == 'CAPA':
      TodayState = 'PA'
      totalDaysPA += 1
      Population = populationIncrease(Population)

  elif TodayState == 'PD':
    Condition = np.random.choice(TransitionStates[1], replace = True, p = TransitionProbabilities[1])

    if Condition == 'PDPD':
      totalDaysPD += 1
      Population = populationDecrease(Population)
    elif Condition == 'PDCA':
      TodayState = 'CA'
      totalDaysCA += 1
    elif Condition == 'PDPA':
      TodayState = 'PA'
      totalDaysPA += 1
      Population = populationIncrease(Population)

  elif TodayState == 'PA':
    Condition = np.random.choice(TransitionStates[2], replace = True, p = TransitionProbabilities[2])

    if Condition == 'PAPA':
      totalDaysPA += 1
      Population = populationIncrease(Population)
    elif Condition == 'PAPD':
      TodayState = 'PD'
      totalDaysPD += 1
      Population = populationDecrease(Population)
    elif Condition == 'PACA':
      TodayState = 'CA'
      totalDaysCA += 1

  if(i % 365 == 0):
    PeopleIncreaseByDay = totalPeopleByDayWithRate(Population)

  QuantityWaterAvailableCarnist = waterConsumptionCarnist(Population, QuantityWaterAvailableCarnist)
  QuantityWaterAvailableVeg = waterConsumptionVeg(Population, QuantityWaterAvailableVeg)

  consumptionWaterCarnistList.append(QuantityWaterAvailableCarnist)
  consumptionWaterVeg.append(QuantityWaterAvailableVeg)
  scenariosList.append(TodayState)

print('Total days CA: ', totalDaysCA)
print('Total days PA: ', totalDaysPA)
print('Total days PD: ', totalDaysPD)

print('\n\nAmount of Water Available Carnist Scenario: ', int(QuantityWaterAvailableCarnist))
print('Amount of Water Available Veg Scenario: ', int(QuantityWaterAvailableVeg))

print('\n\nWater Consumption Carnist Scenario: ', int(9765000000000000000 - QuantityWaterAvailableCarnist))
print('Water Consumption Scenario Veg: ', int(9765000000000000000 - QuantityWaterAvailableVeg))

print('\n\nTotal Population: ', int(Population))

#plt.figure()
#plt.hist(scenariosList)
#plt.show()

plt.figure()
plt.subplot(211)
plt.plot(consumptionWaterCarnistList)
plt.ylabel('Meat Scenario Consumption')

plt.subplot(212)
plt.plot(consumptionWaterVeg)
plt.ylabel('Veg Scenario Consumption')

plt.show()
