class Solution:
    def lower(self, sentence):
        new_s = ""
        for s in sentence:
            n = ord(s)
            if ord("A") <= n <= ord("Z"):
                new_s += chr(n + 32)
            if ord("a") <= n <= ord("z") or ord("0") <= n <= ord("9"):
                new_s += s
            else:
                pass
        return new_s

    def isPalindrome(self, s: str) -> bool:
        s = self.lower(s)
        i = 0
        s_len = len(s)
        while i < s_len // 2:
            j = s_len - 1 - i
            if s[i] != s[j]:
                return False
            i += 1
        return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    # s = "race a car"
    # s = "0P"
    print(Solution().isPalindrome(s))
