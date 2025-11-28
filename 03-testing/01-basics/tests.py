from intervals import overlapping_intervals
from pytest import approx
import pytest

@pytest.mark.parametrize('interval1, interval2', [
    ((1, 5), (3, 6)),
    ((1, 5), (5, 6)),
    ((1, 10), (3, 6)),
    ((6, 8), (3, 6)),
    ((5, 7), (4, 8)),
])
def test_overlapping_intervals(interval1, interval2):
    assert overlapping_intervals(interval1, interval2), f"الفترة {interval1} تتداخل مع الفترة {interval2}"

@pytest.mark.parametrize('interval1, interval2', [
    ((1, 2), (3, 4)),
    ((1, 5), (5, 1)),
    ((8, 9), (6, 7)),
    ((8, 9), (6, 7)),
])
def test_nonoverlapping_intervals(interval1, interval2):
    assert not overlapping_intervals(interval1, interval2), f"الفترة {interval1} لا تتداخل مع الفترة {interval2}"