"""
Module for calculating LCOE

Functions
-------
crf(interest, years)
    Calculates the capital recovery factor
fcost(invest, crf, other, T)
    Calculates the fixed costs
fuel(cost, hw, etha)
    Calculates the fuel costs
co2price(co2, emissionf, etha)
    Calculates the costs of the emitted co2
vcost(co2c, fc, other=0)
    Calculates the variable costs
lcoe(costfix, costvariable)
    calculates the levelized cost of electricity for the power plant
"""


def crf(interest, years):
    """
    Calculates the capital recovery factor

    :param interest: Specifies the interest for the crf
    :param years: Specifies the years for the crf
    :return: capital recovery factor
    """
    return (pow((1 + interest), years)*interest)/(pow((1 + interest), years) - 1)


def fcost(invest, crf, other, T):
    """
    Calculates the fixed costs

    :param invest: Initial investment costs for the power plant in €/MW
    :param crf: Capital recovery factor for that investment
    :param other: Other fixed costs in €/MW
    :param T: Specifies the full load hours in h/a
    :return: fixed costs in €/MWh
    """
    return (crf * invest + other)/T


def fuel(cost, hw=1, etha=1):
    """
    Calculates the fuel costs

    :param cost: Cost of one unit of fuel in €/kg or €/m^3
    :param hw: Specifies the calorific value in kWh/kg or kWh/m^3
    :param etha: Specifies efficiency factor of the technology
    :return: fuel costs in €/MWh
    """
    return (cost/(hw * etha)) * pow(10, 3)


def co2price(co2, emissionf=0, etha=1):
    """
    Calculates the costs of the emitted co2

    :param co2: Cost of co2 emitted in €/t
    :param emissionf: Specifies the emission factor of the technologie in tCo2/MWh
    :param etha: Specifies efficiency factor of the technology
    :return: price of emitted co2 in €/MWh
    """
    return (co2 * emissionf)/etha


def vcost(co2c, fc, other=0):
    """
    Calculates the variable costs

    :param co2p: Cost of co2 emitted in €/MWh
    :param fp: Cost of fuel in €/MWh
    :param other: Specifies other variable costs in €/MWh
    :return: variable costs in €/MWh
    """
    return co2c + fc + other


def lcoe(costfix, costvariable):
    """
      Calculates the LCOE

      :param costfix: fixed cost €/MWh
      :param costvariable: variable cost €/MWh
      :return: Caclulated LCOE
      """
    return costfix + costvariable
