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
	new2 = int(new*(2**((number/3))))
	new3 = int((0.15*new2))
	# hospital beds
	availableBed = int(0.35*data['totalHospitalsBeds'])
	unavailableBed = int(availableBed - new3)
	# print(unavailableBed)
	# icu
	icu = int(0.5*new2)
	# ventilators
	i_ventilators = int(0.2*new2)
	# dollar in flight
	averangedailyincome = data['region']['avgDailyIncomePopulation']
	populationincome = data['region']['avgDailyIncomeInUSD']
	days = number
	dollars = int((new2*averangedailyincome*populationincome)/days)
	# print(dollars)
	impact = {'currentlyInfected': new, 'infectionsByRequestedTime':new2,
				'severeCasesByRequestedTime':new3,
				'hospitalBedsByRequestedTime':unavailableBed,
				'casesForICUByRequestedTime': icu,
				'casesForVentilatorsByRequestedTime':i_ventilators,
				'dollarsInFlight':dollars}
	"""  severe impacts code starts here!"""
	Sia = int(data['reportedCases']*50)
	Sia2 = int(Sia*(2**((number/3))))
	Sia3 = int((0.15*Sia2))
	# hospitalBeds
	sunavailableBed = int(availableBed - Sia3)
	# icu
	s_icu = int(0.5*Sia2)
	# casesForVentilatorsByRequestedTime
	ventilators = int(0.2*Sia2)
	# dollar in flight
	saverangedailyincome = data['region']['avgDailyIncomePopulation']
	spopulationincome = data['region']['avgDailyIncomeInUSD']
	sdays = number
	sdollars = ((Sia2*saverangedailyincome*spopulationincome)/sdays)
	severeImpact = {'currentlyInfected': Sia, 
					'infectionsByRequestedTime':Sia2,
					'severeCasesByRequestedTime':Sia3,
					'hospitalBedsByRequestedTime':sunavailableBed,
					'casesForICUByRequestedTime': s_icu,
					'casesForVentilatorsByRequestedTime':ventilators,
					'dollarsInFlight':sdollars}
	data = {'data':data,'impact':impact,'severeImpact':severeImpact}
	print(data)
	# print(impact,severeImpact)
	return data
# data = {
#      "region":{
#          "name": "africa",
#          "avgAge":19.7,
#          "avgDailyIncomeInUSD":4,
#          "avgDailyIncomePopulation":0.73
#          } ,
#          "periodType":"weeks",
#          "timeToElapse": 38,
#          "reportedCases": 2747,
#          "population":92931687,
#          "totalHospitalsBeds":678874

#       }
# estimator(data)