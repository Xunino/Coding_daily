from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        _str = ""
        for i in digits:
            _str += str(i)
        _str = str(int(_str) + 1)
        return [int(i) for i in _str]

    def plusOne_1(self, digits: List[int]) -> List[int]:
        return [int(i) for i in str(int("".join(map(str, digits))) + 1)]


if __name__ == '__main__':
    digits = [1, 2, 3]
    print(Solution().plusOne(digits))
