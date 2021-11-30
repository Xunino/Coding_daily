class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """
            Create a HashMap (next_greater is dict) from nums2:
                step0: stack append num=1 -> stack(1)
                step1: stack(1) -> len(stack) > 0 and stack[-1]=1 < num=3 -> next_greater{stack.pop()=1: num=3}
                step2: stack(3) -> len(stack) > 0 and stack[-1]=3 < num=4 -> next_greater{stack.pop()=3: num=4}
                step3: stack(4) -> len(stack) > 0 and stack[-1]=4 < num=2 -> not updated into next_greater{1:3, 3:4}
                return: HashMap: next_greater = {1:3, 3:4}
            Get next_greater from nums1 in next_greater:
        """

        stack = []
        next_greater = {}

        for num in nums2:
            while len(stack) != 0 and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        for i in range(len(nums1)):
            if nums1[i] in next_greater.keys():
                nums1[i] = next_greater[nums1[i]]
            else:
                nums1[i] = -1
        return nums1


if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    assert Solution().nextGreaterElement(nums1, nums2) == [-1, 3, -1]

    nums1 = [2, 3, 4, 6]
    nums2 = [6, 4, 3, 1, 2, 7]
    assert Solution().nextGreaterElement(nums1, nums2) == [7, 7, 7, 7]
