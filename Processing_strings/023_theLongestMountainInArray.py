from typing import List


class Solution1:
    def longestMountain(self, arr: List[int]) -> int:
        """
            Time complexity: O(N)
            Extra Space complexity: O(N)
        """
        up = [0] * len(arr)
        for left in range(1, len(arr)):
            if arr[left - 1] < arr[left]:
                up[left] = up[left - 1] + 1

        down = [0] * len(arr)
        for right in range(len(arr) - 1, 0, -1):
            if arr[right] < arr[right - 1]:
                down[right - 1] = down[right] + 1

        result = 0
        for i in range(len(arr)):
            if up[i] > 0 and down[i] > 0:
                result = max(result, up[i] + down[i] + 1)
        return result


class Solution2:
    def longestMountain(self, arr: List[int]) -> int:
        """
            Time complexity: O(N)
            Extra Space complexity: O(1)
        """
        up = 0
        down = 0
        result = 0
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1] or (down and arr[i] < arr[i + 1]):
                up = down = 0
            up += arr[i] < arr[i + 1]
            down += arr[i] > arr[i + 1]
            if up and down:
                result = max(up + down + 1, result)
        return result


class Solution3:
    def longestMountain(self, arr: List[int]) -> int:
        """
            Time complexity: O(N)
            Extra Space complexity: O(1)
        """
        result = 0
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                l = r = i
                while l > 0 and arr[l] > arr[l - 1]:
                    l -= 1
                while r < len(arr) - 1 and arr[r] > arr[r + 1]:
                    r += 1
                result = max(r - l + 1, result)
        return result


if __name__ == '__main__':
    matrix = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # matrix = [2, 2, 2]
    print(Solution1().longestMountain(matrix))
    print(Solution2().longestMountain(matrix))
    print(Solution3().longestMountain(matrix))
