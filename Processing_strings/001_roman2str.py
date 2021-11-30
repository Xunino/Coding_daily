class Solution:
    def romanToInt(self, s: str) -> int:
        self.roman2str = {'I': 1,
                          'V': 5,
                          'X': 10,
                          'L': 50,
                          'C': 100,
                          'D': 500,
                          'M': 1000}
        """
            1. Chỉ có 1 chữ
            2. Có 2 chữ trở lên
                - TH1: Các chữ đặc biệt: IV: 4, IX: 9, XL: 40, XC: 90, CD: 400, CM: 900
                - TH2: Các trường hợp còn lại 
        """
        if s in self.roman2str:
            return self.roman2str[s]

        result = self.roman2str[s[0]]  # 1
        prev = s[0]
        for elem in s[1:]:
            if self.roman2str[prev] < self.roman2str[elem]:
                result += self.roman2str[elem] - self.roman2str[prev] - self.roman2str[prev]  # 1 + 5 - 1 - 1
            else:
                result += self.roman2str[elem]
            prev = elem
        return result


if __name__ == '__main__':
    print(Solution().romanToInt("CMXLXC"))
