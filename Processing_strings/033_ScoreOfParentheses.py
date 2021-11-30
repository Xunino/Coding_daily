class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0
        for i in range(len(s)):
            score = 0
            if s[i] == "(":
                stack.append(score)
            else:
                while stack[-1] != 0:
                    score += stack.pop()
                score = max(2 * score, 1)
                stack.pop()
                stack.append(score)

        for i in stack:
            result += i

        return result if result != 0 else result


if __name__ == '__main__':
    s = "(()(()))"
    print(Solution().scoreOfParentheses(s))
