class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            stack.append(c)
            while len(stack) >= 3 and stack[-1] == "c" and stack[-2] == "b" and stack[-3] == "a":
                stack.pop()
                stack.pop()
                stack.pop()
        return not stack


if __name__ == '__main__':
    s = "abcabcabc"
    print(Solution().isValid(s))
