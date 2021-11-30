from typing import List


class Solution_1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            Idea:
                - Xóa 1 phần tử thứ i trong mảng
                - Tính tích các phần từ trong mảng đó
                - Cập nhật giá trị vào vị trí thứ i
        """
        values = []
        num_len = len(nums)
        for i in range(num_len):
            times = 1
            n_nums = nums.copy()
            n_nums.pop(n_nums.index(n_nums[i]))
            for num in n_nums:
                times *= num
            values.append(times)
        return values


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         m = len(nums)
#         values = []
#         times = 1
#         for i in range(m):
#             values.append(times)
#             times = times * nums[i]
#
#         times = 1
#         for i in range(m - 1, -1, -1):
#             values[i] = values[i] * times
#             times *= nums[i]
#         print(values)


if __name__ == '__main__':
    nums = [-1, 1, 0, -3, 3]
    print(Solution_1().productExceptSelf(nums))
