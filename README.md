# LCOE-calculator

A small python script that calculates the LCOE of a power plant. The necessary data of the power plant must be entered in main.py. The function.py file contains following functions:

-crf(interest, years)  
    Calculates the capital recovery factor  
-fcost(invest, crf, other, T)  
    Calculates the fixed costs  
-fuel(cost, hw, etha)  
    Calculates the fuel costs  
-co2price(co2, emissionf, etha)  
    Calculates the costs of the emitted co2  
-vcost(co2c, fc, other=0)  
    Calculates the variable costs  
-lcoe(costfix, costvariable)  
    calculates the levelized cost of electricity for the power plant  


Copyright 2023 Sandro Gmeiner

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
