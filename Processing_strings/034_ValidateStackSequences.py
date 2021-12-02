class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        i = 0
        stack = []
        for p in pushed:
            stack.append(p)
            while len(stack) != 0 and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack


if __name__ == '__main__':
    """
    I, Compare pushed vs popped:
                              !
        pushed = [1, 2, 3, 4, 5]
                  
        i = 0
                  i 
        popped = [4, 5, 3, 2, 1]
        
        4 != 1: -> stack(1)
        4 != 2: -> stack(1, 2)
        4 != 3: -> stack(1, 2, 3)
        4 == 4: -> stack(1, 2, 3, 4)
        4 != 5: -> in while: 
                1. pop() -> stack(1, 2, 3, 5)
                2. i = 1
    
    II, When i = 1 and pushed haven't values to comparing, then this is time to pop/compare popped with stack. 

    i = 1
                       !
    stack  = [1, 2, 3, 5]
                 i
    popped = [4, 5, 3, 2, 1]
    -> stack.pop()
    
    i = 2
                    !
    stack  = [1, 2, 3]
                    i
    popped = [4, 5, 3, 2, 1]
    -> stack.pop()
    
    i = 3
                 !
    stack  = [1, 2]
                       i
    popped = [4, 5, 3, 2, 1]
    -> stack.pop()
    
    i = 4
              !
    stack  = [1]
                          i
    popped = [4, 5, 3, 2, 1]
    -> stack.pop()
    
    -> stack is empty
        
    """
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    print(Solution().validateStackSequences(pushed, popped))
