from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_list = []
        _sum = 0
        for i in nums:
            _sum += i
            new_list.append(_sum)
        return new_list
