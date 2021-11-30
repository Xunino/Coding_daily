class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) <= 1:
            return s

        s = list(s)
        for i in range(0, len(s), 2 * k):
            if len(s[i: i + k]) < k:
                k = len(s[i: i + k])

            new_s = s[i: i + k]
            n = 0
            while n < k // 2:
                m = k - n - 1
                new_s[n], new_s[m] = new_s[m], new_s[n]
                n += 1
            s[i: i + k] = new_s
        return "".join(s)


if __name__ == '__main__':
    s = "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"
    k = 39
    print(Solution().reverseStr(s, k))
