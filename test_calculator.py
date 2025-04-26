import pytest
from calculator import Calculator

# def test_multiply_int_and_float():
#     calc = Calculator()
#     assert calc.multiply(3, 4) == 12
#     assert pytest.approx(calc.multiply(2.5, 4.0), rel=1e-9) == 10.0

# def test_divide_various_cases():
#     calc = Calculator()
#     assert calc.divide(10, 2) == 5
#     assert pytest.approx(calc.divide(5, 2), rel=1e-9) == 2.5
#     with pytest.raises(ValueError):
#         calc.divide(5, 0)


# def test_add():
#     calc = Calculator()
#     assert calc.add(3, 5) == 8
#     assert calc.add(-1, 1) == 0
#     assert calc.add(-1, -1) == -2

# def test_subtract():
#     calc = Calculator()
#     assert calc.subtract(5, 3) == 2
#     assert calc.subtract(1, 5) == -4
#     assert calc.subtract(-5, -3) == -2


#---------------------------------------------------------------
# @pytest.mark.parametrize("a,b,exp", [(3,5,8),(-1,1,0),(-1,-1,-2),(0,0,0)])
# def test_add_param(a,b,exp):
#     assert Calculator().add(a,b) == exp

# @pytest.mark.parametrize("a,b,exp", [(5,3,2),(1,5,-4),(-5,-3,-2)])
# def test_subtract_param(a,b,exp):
#     assert Calculator().subtract(a,b) == exp

# @pytest.mark.parametrize("a,b,exp", [(3,4,12),(2.5,4.0,10.0)])
# def test_multiply_param(a,b,exp):
#     assert pytest.approx(Calculator().multiply(a,b),1e-9) == exp

# @pytest.mark.parametrize("a,b,exp", [(10,2,5),(5,2,2.5)])
# def test_divide_param(a,b,exp):
#     assert pytest.approx(Calculator().divide(a,b),1e-9) == exp

#-----------------------------------------------------------
@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0),
])
def test_add_parameterized(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1, 5, -4),
    (-5, -3, -2),
])
def test_subtract_parameterized(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (2.5, 4.0, 10.0),
])
def test_multiply_parameterized(calculator, a, b, expected):
    assert pytest.approx(calculator.multiply(a, b), rel=1e-9) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5),
])
def test_divide_parameterized(calculator, a, b, expected):
    assert pytest.approx(calculator.divide(a, b), rel=1e-9) == expected

import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (3, 2, 9),
    (2, 0, 1),
])
def test_power_positive(calculator, a, b, expected):
    assert calculator.power(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, -2, 0.25),
    (10, -1, 0.1),
])
def test_power_negative(calculator, a, b, expected):
    assert pytest.approx(calculator.power(a, b), rel=1e-9) == expected


@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (5, 120),
])
def test_factorial_normal(calculator, n, expected):
    assert calculator.factorial(n) == expected

def test_factorial_negative(calculator):
    with pytest.raises(ValueError):
        calculator.factorial(-3)

@pytest.mark.parametrize("n, expected", [
    (0, 0), 
    (1, 1),  
    (7, 13),
])
def test_fibonacci_normal(calculator, n, expected):
    assert calculator.fibonacci(n) == expected

def test_fibonacci_negative(calculator):
    with pytest.raises(ValueError):
        calculator.fibonacci(-5)

# def test_precise_add_rounds_to_two_decimal_places(precise_calculator):
#     result = precise_calculator.add(1.2345, 2.3456)
#     assert pytest.approx(result, rel=1e-9) == 3.58


def test_rounding_at_various_precisions(precise_calculator):
    a, b = 1.23456, 2.34567
    prec = precise_calculator.precision

    raw_add = a + b
    expected_add = round(raw_add, prec)
    assert precise_calculator.add(a, b) == expected_add

    raw_mul = a * b
    expected_mul = round(raw_mul, prec)
    assert precise_calculator.multiply(a, b) == expected_mul

