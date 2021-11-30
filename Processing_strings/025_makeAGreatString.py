class Solution:
    """
        B1: Tạo một stack
        B2: Lặp qua các phần từ trong chuỗi
        B3: Kiểm tra stack:
            - Nếu stack rỗng thêm phần tử vào stack
            - Nếu stack k rỗng kiểm tra phần từ cuối cùng của stack
                - Kiểm tra phần tử cuối cùng của stack
                    - Giống ký tự hiện tại pop ra khỏi stack
                    - K giống thì thêm phần tử vào stack
    """
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
                continue
            if stack[-1] == i.swapcase():
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)


if __name__ == '__main__':
    s = "leEeetcode"
    print(Solution().makeGood(s))
