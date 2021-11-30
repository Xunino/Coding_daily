from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        stacks = []
        count = 1
        for i in range(len(chars)):
            if len(stacks) == 0:
                stacks.append((chars[i], count))
                continue

            if stacks[-1][0] == chars[i]:
                count += 1
                stacks.pop()
                stacks.append((chars[i], count))
            else:
                count = 1
                stacks.append((chars[i], count))

        new_s = ""
        for s in range(len(stacks)):
            if stacks[s][1] == 1:
                new_s += str(stacks[s][0])
            else:
                new_s += stacks[s][0] + str(stacks[s][1])

        for s in range(len(new_s)):
            chars[s] = new_s[s]

        return len(new_s)


if __name__ == '__main__':
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    # chars = ["a"]
    # chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    print(Solution().compress(chars))
