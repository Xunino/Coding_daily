class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        return len(set(words)) == len(set(pattern)) == len(set(zip(words, pattern)))


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    print(Solution().wordPattern(pattern, s))
