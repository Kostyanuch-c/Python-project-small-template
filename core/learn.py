class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums)

        while start < end:
            middle = (start + end) // 2
            middle_num = nums[middle]
            if target > middle_num:
                start = middle + 1
            else:
                end = middle
        return start


print(Solution().searchInsert([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
