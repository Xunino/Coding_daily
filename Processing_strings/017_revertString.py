from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_len = len(s)
        i = 0
        j = s_len - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    print(Solution().reverseString(s))
