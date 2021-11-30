import collections


class Solution:
    def balancedString(self, s: str) -> int:
        max_chars = len(s) // 4
        counter = collections.Counter(s)

        hash_str = {}
        for key in counter.keys():
            if counter[key] > max_chars:
                hash_str[key] = counter[key] - max_chars

        if len(hash_str) == 0:
            return 0

        result = len(s)
        i, j = 0, 0
        while j < len(s):
            if s[j] in hash_str:
                hash_str[s[j]] -= 1

                while max(hash_str.values()) <= 0:
                    result = min(result, j - i + 1)
                    if s[i] in hash_str:
                        hash_str[s[i]] += 1
                    i += 1
            j += 1

        return result


if __name__ == '__main__':
    # assert Solution().balancedString("QQER") == 1
    print(Solution().balancedString("ABBCCA"))
