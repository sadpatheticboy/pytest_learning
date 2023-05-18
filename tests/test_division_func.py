from utils import division
import pytest


@pytest.mark.parametrize('a, b, expected_result', [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize('expected_excpetion, dividend, divider', [(ZeroDivisionError, 10, 0),
                                                         (TypeError, 20, '2')])
def test_zero_division(expected_excpetion, dividend, divider):
    with pytest.raises(expected_excpetion):
        division(dividend, divider)
