class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        """
            Tính khoảng các giữa 2 phần tử:
            
            + Thêm 1 phần tử và chỉ mục vào stack
            
            + Kiểm tra phần tử trong stack:
                - Nếu stack != 0 và phần từ cuối cùng trong stack > giá trị hiện tại
                    -> tính khoảng cách 
                - Nếu stack != 0 và phần tử cuối trong stack < giá trị hiện tại
                    -> xoá phần tử cuối đi
        """

        stack = []
        distances = [0] * len(temperatures)
        for idx in range(len(temperatures) - 1, -1, -1):
            # Checking element in stack with current temperature
            while len(stack) != 0 and temperatures[idx] >= stack[-1][0]:
                stack.pop()

            # Compute distance
            for s in stack:
                if temperatures[idx] < s[0]:
                    distances[idx] = s[1] - idx

            # Add element into stack
            stack.append((temperatures[idx], idx))
        return distances


if __name__ == '__main__':
    T = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    print(Solution().dailyTemperatures(T))
