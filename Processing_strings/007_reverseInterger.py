class Solution:
    def reverse(self, x: int) -> int:
        _str = str(x)
        len_x = len(_str)
        new = ""

        if x < 0:
            new += "-"
            for i in range(len_x - 1, 0, -1):
                new += _str[i]
        else:
            for i in range(len_x - 1, -1, -1):
                new += _str[i]

        if int(new) < -2 ** 31 or int(new) > 2 ** 31 - 1:
            return 0
        else:
            return int(new)


if __name__ == '__main__':
    i = 1534236469

    print(Solution().reverse(i))
