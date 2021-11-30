from collections import defaultdict


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = defaultdict(int)
        for i in s:
            s_dict[i] += 1

        for i in t:
            s_dict[i] -= 1

        return sum([x for x in s_dict.values() if x > 0])


if __name__ == '__main__':
    s = "leetcode"
    t = "practice"
    print(Solution().minSteps(s, t))
