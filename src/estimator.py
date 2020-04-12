import math
from pprint import pprint
def estimator(data):
	# print(data['periodType'])
	raw = data['periodType']
	number = data['timeToElapse']
	if raw =='days':
		number = number
	if raw  == 'months':
		number = number*30
	if raw == 'weeks':
		number = number*7
	print(number)
	new = int(data['reportedCases']*10)
	new2 = int(new*(2**(math.trunc(number/3))))
	print(new2)
	new3 = int((0.15*new2))
	# hospital beds
	availableBed =(0.35*data['totalHospitalBeds'])
	# print(availableBed)
	unavailableBed = int(availableBed - new3)
	# print(unavailableBed)
	# print(unavailableBed)
	# icu
	icu = (0.05*new2)
	print(icu)
	# ventilators
	i_ventilators = int(0.02*new2)
	# dollar in flight
	averangedailyincome = data['region']['avgDailyIncomePopulation']
	populationincome = data['region']['avgDailyIncomeInUSD']
	days = number
	dollars = round((new2*averangedailyincome*populationincome)/days,1)
	# print(dollars)
	impact = {'currentlyInfected': new,
            'infectionsByRequestedTime':new2,
			'severeCasesByRequestedTime':new3,
			'hospitalBedsByRequestedTime':unavailableBed,
			'casesForICUByRequestedTime': icu,
			'casesForVentilatorsByRequestedTime':i_ventilators,
			'dollarsInFlight':dollars}
	"""  severe impacts code starts here!"""
	Sia = int(data['reportedCases']*50)
	Sia2 = int(Sia*(2**(math.trunc(number/3))))
	Sia3 = int((0.15*Sia2))
	# hospitalBeds
	sunavailableBed = int(availableBed - Sia3)
	# icu
	s_icu = int(0.05*Sia2)
	# casesForVentilatorsByRequestedTime
	ventilators = int(0.02*Sia2)
	# dollar in flight
	saverangedailyincome = data['region']['avgDailyIncomePopulation']
	spopulationincome = data['region']['avgDailyIncomeInUSD']
	sdays = number
	sdollars = round((Sia2*saverangedailyincome*spopulationincome)/sdays,1)
	severeImpact = {'currentlyInfected': Sia, 
					'infectionsByRequestedTime':Sia2,
					'severeCasesByRequestedTime':Sia3,
					'hospitalBedsByRequestedTime':sunavailableBed,
					'casesForICUByRequestedTime': s_icu,
					'casesForVentilatorsByRequestedTime':ventilators,
					'dollarsInFlight':sdollars}
	data = {'data':data,'impact':impact,'severeImpact':severeImpact}
	# print(data)
	print(impact,severeImpact)
	return data
data = {
     "region":{
         "name": "africa",
         "avgAge":19.7,
         "avgDailyIncomeInUSD":4,
         "avgDailyIncomePopulation":0.73
         } ,
         "periodType":"days",
         "timeToElapse": 38,
         "reportedCases": 2747,
         "population":92931687,
         "totalHospitalBeds":678874

      }
estimator(data)