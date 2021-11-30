class Solution:
    def toLowerCase(self, s: str) -> str:
        l = ""
        for i in s:
            check = ord(i)
            if 65 <= check <= 90:
                l += chr(check + 32)
            else:
                l += chr(check)
        return l


if __name__ == '__main__':
    num = "Hello"
    print(Solution().toLowerCase(num))
