class Solution:

    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')

        s = list(s)
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]

            elif s[left] not in vowels:
                left += 1
                continue

            elif s[right] not in vowels:
                right -= 1
                continue

            left += 1
            right -= 1

        return "".join(s)

    def reversVowels_2(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")
        stack = [c for c in s if c in vowels]
        new_s = ""
        for c in s:
            if c in vowels:
                new_s += stack.pop()
            else:
                new_s += c
        return new_s


if __name__ == '__main__':
    s = "leetcode"
    assert Solution().reversVowels_2(s) == "leotcede"
