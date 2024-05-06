from math import sqrt
from typing import List


def task1(nums: List[int]) -> List[int]:
    return list(set(nums))


def _is_simple(num):
    return all([bool(num % i) for i in range(2, num)])


def task2(mn: int, mx: int) -> List[int]:
    nums = [i for i in range(mn, mx + 1) if _is_simple(i)]
    return nums


def task4(strs: List[str], reverse=False) -> List[str]:
    if reverse:
        return sorted(strs, key=lambda x: -len(x))
    return sorted(strs, key=len)


class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def set_x(self, x: float) -> None:
        self._x = x

    def set_y(self, y: float) -> None:
        self._y = y

    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    def eval_distance(self, other) -> float:
        other_x = other.get_x()
        other_y = other.get_y()
        return sqrt((other_x - self._x) ** 2 + (other_y - self._y) ** 2)


if __name__ == '__main__':
    # tests

    # task 1
    assert task1([1, 1, 1]) == [1], task1([1, 1, 1])
    assert task1([]) == [], task1([])
    assert set(task1([3, 1, 3, 2, 3, 6, 4, 0])) == {3, 1, 2, 6, 4, 0}, task1([3, 1, 3, 2, 3, 6, 4, 0])

    # task 2
    assert not _is_simple(4)
    assert _is_simple(5)
    assert _is_simple(19)
    assert not _is_simple(22)
    assert _is_simple(163)

    assert task2(4, 10) == [5, 7], task2(4, 10)
    assert task2(2, 100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                             89, 97], task2(2, 100)
    assert task2(9, 10) == [], task2(9, 10)

    # task 3
    point1 = Point(1, 1)
    point2 = Point(1, 5)

    assert point1.eval_distance(point2) == 4, point1.eval_distance(point2)
    assert point2.eval_distance(point1) == 4, point2.eval_distance(point1)

    # task 4
    assert task4(['a', 'abc', 'ab']) == ['a', 'ab', 'abc'], task4(['a', 'abc', 'ab'])
    assert task4(['a', 'abc', 'ab'], reverse=True) == ['abc', 'ab', 'a'], task4(['a', 'abc', 'ab'])
