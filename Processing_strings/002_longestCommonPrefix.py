from typing import List


class Solution:
    """
        1. Lấy word_1 bất kỳ trong array là giá trị tạp thời
        2. Xóa ward_1 vừa lấy ra khỏi array
        3. So sánh phần tử trong array với word_1, nếu k có phần từ tiếp theo trùng nhau thì break
        4. Cập nhật phần tử trùng nhau => word_1 để so sánh với từ tiếp theo trong array
        5. Return word_1
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        str_0 = strs[0]
        for elem in strs[1:]:
            candidate = ""
            for i in range(min(len(str_0), len(elem))):
                if str_0[i] == elem[i]:
                    candidate += str_0[i]
                else:
                    break
            str_0 = candidate
        return str_0


if __name__ == '__main__':
    strs = [["flower", "flow", "flight"],
            ["cir", "car"],
            ["reflower", "flow", "flight"],
            ["flower", "flower", "flower", "flower"],
            ["flower", "fkow"],
            ["flower", "flow", "flight"],
            ["aaa", "aa", "aaa"]]
    for i in strs:
        print(Solution().longestCommonPrefix(i))
