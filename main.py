"""
Main script for calculating the LCOE of a powerplant

"""
import functions as func

'''
Data of power plant
'''
# GuD
name = 'GuD'  # name of power plant
r = 0.04  # interest rate
n = 35  # operational time in years
etha = 0.59  # efficency
invest = 870000  # specific investment costs in €/MW
maintain_fixed = 32000  # fixed maintenance cost in €/MW/a
maintain_var = 2.3  # variable maintenance cost €/MWh
t = 3000  # full load hours in h/a
emission_factor = 0.2  # emission factor in tCo2/MWh
fuel_hw = 10  # used fuel in kWh/kg or m^3
fuel_price = 0.3  # price of fuel in €/kg or €/m^3
co2_price = 10  # in €/t

crf = func.crf(r, n)
fixed_cost = func.fcost(invest, crf, maintain_fixed, t)
fuel_cost = func.fuel(fuel_price, fuel_hw, etha)
co2_cost = func.co2price(co2_price, emission_factor, etha)
variable_cost = func.vcost(co2_cost, fuel_cost, maintain_var)

print('The LCOE of the ' + name + ' are ' + str(func.lcoe(fixed_cost, variable_cost)) + ' €/MWh')
print('The fixed costs are ' + str(fixed_cost) + ' €/MWh ')
print('The variable costs are ' + str(variable_cost) + ' €/MWh ')

