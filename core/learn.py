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


if __name__ == "__main__":
    solution = Solution()
    args = [1, 2, 4, 5, 6, 7]
    print(solution.searchInsert(args, 3))
