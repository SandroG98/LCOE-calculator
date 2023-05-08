'''
File for testing the functions module
'''

import functions as func
import math


def test_crf():
    assert math.isclose(func.crf(0.05, 10), 0.10, rel_tol=0.0001) == 1


def test_fcost():
    assert math.isclose(func.fcost(10, 2, 10, 5), 6, rel_tol=0.0001) == 1


def test_fuel():
    assert math.isclose(func.fuel(10, 10, 0.5), 2000, rel_tol=0.0001) == 1


def test_co2price():
    assert math.isclose(func.co2price(10, 10, 0.5), 200, rel_tol=0.0001) == 1


def test_vcost():
    assert func.vcost(5, 3, 2) == 10


def test_lcoe():
    assert func.lcoe(5, 2)==8
