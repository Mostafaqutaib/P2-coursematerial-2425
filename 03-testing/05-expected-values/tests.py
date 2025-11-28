import pytest
from mergesort import split_in_two, merge_sorted


@pytest.mark.parametrize('ns', [
    list(range(n)) for n in range(0, 10)
])
def test_split_in_two(ns):
    left, right = split_in_two(ns)

    # 1) ما فقدنا ولا عنصر ولا أضفنا
    assert left + right == ns, 'left and right together should reconstruct the original list'

    # 2) فرق الطول بين القائمتين <= 1
    assert abs(len(left) - len(right)) <= 1, (
        f'lengths differ too much: len(left)={len(left)}, len(right)={len(right)}'
    )

sorted_lists = [
    [],
    [1],
    [1, 2],
    [1, 3, 5],
    [2, 2, 4, 6],
    [1, 4, 7, 10],
    [3, 3, 3],
    [1, 5, 9, 15, 20],
]

@pytest.mark.parametrize('left', sorted_lists)
@pytest.mark.parametrize('right', sorted_lists)
def test_merge_sorted(left, right):
    actual = merge_sorted(left, right)
    expected = sorted(left + right)
    assert actual == expected, f"merge_sorted({left}, {right}) = {actual}, but expected {expected}"