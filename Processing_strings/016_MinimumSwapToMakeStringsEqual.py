class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        m = len(s2)
        s1 = list(s1)
        s2 = list(s2)

        new_s1 = []
        new_s2 = []
        for i in range(m):
            if s1[i] != s2[i]:
                new_s1.append(s1[i])
                new_s2.append(s2[i])

        print(new_s1)
        print(new_s2)


if __name__ == '__main__':
    s1 = "xxyyxyxyxx"
    s2 = "xyyxyxxxyx"
    Solution().minimumSwap(s1, s2)
