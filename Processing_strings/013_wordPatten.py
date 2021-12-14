class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        return len(set(words)) == len(set(pattern)) == len(set(zip(words, pattern)))

    def wordPattern_2(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        hashtable = {}
        for i in range(len(words)):
            if pattern[i] not in hashtable:
                if words[i] in hashtable.values():
                    return False
                hashtable[pattern[i]] = words[i]
            else:
                if hashtable[pattern[i]] != words[i]:
                    return False
        return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    print(Solution().wordPattern(pattern, s))
    print(Solution().wordPattern_2(pattern, s))
