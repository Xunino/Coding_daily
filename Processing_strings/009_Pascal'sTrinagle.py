from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1] * (i + 1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j] + pascal[i - 1][j - 1]
        return pascal


if __name__ == '__main__':
    num = 5
    print(Solution().generate(num))
