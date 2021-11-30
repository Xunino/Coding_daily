class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        ## Ý tưởng. 
            # 1. Thực hiện việc kiểm tra độ chính xác đầy đủ của ký tự đóng và mở ngoặc như thông thường. 
            # 2. Loại bỏ ký tự "(" hoặc ")" thừa trong chuỗi
            ## Cách code
            # 1. Tạo stack = []
            # 2. Chuyển s thành mảng s = list(s)
            # 3. Lặp qua các ký tự trong mảng này. Ở mỗi vòng lặp
            # - 3.1. Nếu ký tự này là mở ngoặc "(" thì thêm chỉ mục ký tự này vào stack
            # - 3.2. Nếu ký tự này là đóng ngoặc ")" thì:
            # -- 3.2.1. Nếu stack không rỗng thì xóa chỉ mục ký tự "(" tương ứng của ký tự này ra khỏi stack
            # -- 3.2.2. Nếu stack rỗng, tức là ký tự ")" này là thừa, set s[i] = ''
            # 4. Nếu stack vẫn còn phần tử tức là có các ký tự "(" thừa,
            # - 4.1. Pop các chỉ mục này và đặt giá trị của chỉ mục này trong s là '': s[stack.pop()] = ''
            # 5. Trả về chuỗi mới nối bởi những phần tử trong mảng s: "".join(s)
        """
        stack = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    s[i] = ""

            elif s[i] == "(":
                stack.append((s[i], i))

        while stack:
            s[stack.pop()[1]] = ""

        return "".join(s)


if __name__ == '__main__':
    # s = "lee(t(c)o)de)"
    s = "))(("
    print(Solution().minRemoveToMakeValid(s))
