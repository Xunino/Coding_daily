class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in set(s):
            if s.count(i) == t.count(i):
                pass
            else:
                return False

        true_len = len(s)
        count = 0
        for i in s:
            if i in t:
                count += 1
        if count == true_len:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))
