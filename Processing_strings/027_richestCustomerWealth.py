from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])


if __name__ == '__main__':
    accounts = [[1, 5], [7, 3], [3, 5]]
    print(Solution().maximumWealth(accounts))
