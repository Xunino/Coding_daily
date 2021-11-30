class Solution:
    def split(self, sentence):
        new_s = []
        s = ""
        for w in sentence + " ":
            if w != " ":
                s += w
            else:
                new_s.append(s)
                s = ""
        return "".join(new_s)

    def lower(self, sentence):
        new_s = ""
        for w in self.split(sentence):
            if ord("A") <= ord(w) <= ord("Z"):
                new_s += chr(ord(w) + 32)
            else:
                new_s += w
        return new_s

    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiou')
        new_s = ""
        for w in self.lower(s):
            if w not in vowels:
                new_s += w
        return new_s


if __name__ == '__main__':
    s = "leet code is a community for coder"
    print(Solution().reverseVowels(s))
