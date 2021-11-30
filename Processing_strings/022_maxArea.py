from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max_area = 0
        # for l in range(len(height)):
        #     for r in range(l + 1, len(height)):
        #         area = (r - l) * min(height[l], height[r])
        #         max_area = max(area, max_area)
        # return max_area

        l = 0
        max_area = 0
        r = len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(area, max_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


if __name__ == '__main__':
    matrix = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(matrix))
