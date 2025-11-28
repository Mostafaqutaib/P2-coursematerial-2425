import pytest
from mystatistics import average
from pytest import approx

@pytest.mark.parametrize('ns, expected', [
    ([0.1, 0.1, 0.1], 0.1),
    ([1, 2, 3], 2),
    ([1.5, 2.5, 3.5], 2.5),
    ([0, 0, 0], 0),
    ([1], 1),
    ([1, 3], 2),
    ([0.1, 0.2, 0.3], 0.2),
    ([10.5, 20.5, 30.5], 20.5),
    ([], 0),  # قائمة فارغة
])
def test_average(ns, expected):
    actual = average(ns)
    assert approx(expected, abs=0.01) == actual, f"المتوسط لـ {ns} يجب أن يكون {expected} تقريباً، لكن كان {actual}"