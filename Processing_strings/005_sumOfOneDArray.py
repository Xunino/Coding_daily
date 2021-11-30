from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_list = []
        _sum = 0
        for i in nums:
            _sum += i
            new_list.append(_sum)
        return new_list


if __name__ == '__main__':
    arr = [1, 1, 2, 3, 4, 5]
    print(Solution().runningSum(arr))
