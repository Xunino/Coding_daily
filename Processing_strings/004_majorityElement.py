from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in set(nums):
            count = nums.count(i)
            if count > len(nums) / 2:
                return i


if __name__ == '__main__':
    arr = [2, 2, 2, 1, 1, 1, 2]
    Solution().majorityElement(arr)
