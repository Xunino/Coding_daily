class Solution:
    def split(self, sentence):
        s_list = []
        n_s = ""
        for s in sentence + " ":
            if s != " ":
                n_s += s
            else:
                s_list.append(n_s)
                n_s = ""
        return s_list

    def reverseWords(self, s: str) -> str:
        s = self.split(s)
        new_s = []
        for w in s:
            w = list(w)
            n = 0
            while n < len(w) // 2:
                m = len(w) - n - 1
                w[n], w[m] = w[m], w[n]
                n += 1
            new_s.append("".join(w))
        return " ".join(new_s)


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print(Solution().reverseWords(s))
