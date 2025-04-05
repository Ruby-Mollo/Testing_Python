import pytest
from suma import sumar

@pytest.mark.parametrize("num1, num2, resultado", {
    (1,2,3),
    (4,5,9),
    (-2,-4,-2)
})
def test_suma_parametrizada(num1,num2,resultado):
    assert sumar(num1,num2) == resultado, "Ta mal"