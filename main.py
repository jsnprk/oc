from local_settings import *
from Portfolio import Portfolio

#https://fred.stlouisfed.org/series/A25BVS
#https://fred.stlouisfed.org/series/A25BTI
#https://fred.stlouisfed.org/series/MRTSSM44611USS
#https://fred.stlouisfed.org/series/SMU36000003232540001SA

cfg = {
  'A25BVS' : "Manufacturers' Value of Shipments: Pharmaceutical and Medicine Manufacturing",
  'A25BTI' : "Manufacturers' Total Inventories: Pharmaceutical and Medicine Manufacturing",
  'MRTSSM44611USS' : 'Retail Sales: Pharmacies and Drug Stores',
  'SMU36000003232540001SA' : 'All Employees: Manufacturing: Non-Durable Goods: Pharmaceutical and Medicine Manufacturing in New York'
}

p = Portfolio( 'Healthcare', cfg )
p.initGrowthRates()
p.compareGrowthRatesForDate('2023-07-01')
p.plotAllIndicators('growthRate')
