import pytest
from search import linear_search, binary_search
from student import Student

def make_students(ids):
    return [Student(id) for id in ids]


@pytest.mark.parametrize('students, target_id', [

    # empty list
    (make_students([]), 10),

    # first student
    (make_students([5, 10, 20, 30]), 5),

    # middle student
    (make_students([5, 10, 20, 30]), 20),

    # last student
    (make_students([5, 10, 20, 30]), 30),

    # id too small
    (make_students([5, 10, 20, 30]), 0),

    # id too large
    (make_students([5, 10, 20, 30]), 100),

    # gaps + found
    (make_students([3, 7, 100]), 7),

    # gaps + not found
    (make_students([3, 7, 100]), 50),
])
def test_linear_and_binary_agree(students, target_id):
    expected = linear_search(students, target_id)
    actual = binary_search(students, target_id)
    assert actual == expected
