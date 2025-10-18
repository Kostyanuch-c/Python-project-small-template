import pytest

from core import learn


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([], 2, 0),
        ([1, 2, 4, 5, 6, 7], 3, 2),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 9),
        ([2, 3, 4, 5, 6, 7, 8, 9], 1, 0),
    ],
)
def test_search_insert(nums: list[int], target: int, expected: int) -> None:
    assert learn.Solution().searchInsert(nums, target) == expected
