import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

class PreciseCalculator(Calculator):
    def __init__(self, precision=2):
        super().__init__()
        self.precision = precision

    def add(self, a, b):
        result = super().add(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def subtract(self, a, b):
        result = super().subtract(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def multiply(self, a, b):
        result = super().multiply(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def divide(self, a, b):
        result = super().divide(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def power(self, a, b):
        result = super().power(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def factorial(self, n):
        result = super().factorial(n)
        return round(result, self.precision) if isinstance(result, float) else result

    def fibonacci(self, n):
        result = super().fibonacci(n)
        return round(result, self.precision) if isinstance(result, float) else result

# @pytest.fixture
# def precise_calculator():
#     return PreciseCalculator(precision=2)

class PreciseCalculator(Calculator):
    def __init__(self, precision=2):
        super().__init__()
        self.precision = precision
    def add(self, a, b):
        r = super().add(a, b)
        return round(r, self.precision) if isinstance(r, float) else r
    def multiply(self, a, b):
        r = super().multiply(a, b)
        return round(r, self.precision) if isinstance(r, float) else r


# parameterize over three different precision levels
@pytest.fixture(params=[1, 2, 3])
def precise_calculator(request):
    return PreciseCalculator(precision=request.param)