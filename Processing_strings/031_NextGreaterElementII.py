class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        stack = []
        results = [-1] * n
        for i in range(1, 2 * len(nums)):
            while len(stack) != 0 and nums[i % n] > nums[stack[-1]]:
                results[stack.pop()] = nums[i % n]
            stack.append(i % n)  # index 0
        return results


if __name__ == '__main__':
    nums = [5, 4, 3, 2, 1]
    print(Solution().nextGreaterElements(nums))
