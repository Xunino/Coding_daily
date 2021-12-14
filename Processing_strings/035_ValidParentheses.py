class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if not stack and i in hashmap:
                stack.append(i)
                break
            else:
                if i not in hashmap:
                    stack.append(i)
                else:
                    if stack[-1] != hashmap[i]:
                        stack.append(i)
                        continue

                    while stack and stack[-1] == hashmap[i]:
                        stack.pop()
                        break
        return not stack


if __name__ == '__main__':
    a = ["]", "(]", "([)]", "{[]}", "({{{{}}}))", "[[[]", "(])"]
    for i in a:
        print(Solution().isValid(i))

    """
    1
    ( { { { { } } } ) )
    -> add "("
    
      2
    ( { { { { } } } ) )
    -> add "{"
    
        3
    ( { { { { } } } ) )
    -> add "{"
    
          4
    ( { { { { } } } ) )
    -> add "{"
    
            5
    ( { { { { } } } ) )
    -> add "{"
    
              6 7 8 9 10
    ( { { { { } } } ) )  
    -> hashmap[stack[-1]] || stack = [(, {, {, {, {]
        - If this is hashmap[6](="{") == stack(="{") -> pop() break
        - If this is hashmap[7](="{") == stack(="{") -> pop() break
        - If this is hashmap[8](="{") == stack(="{") -> pop() break
        - If this is hashmap[9](="(") != stack(="{") -> out 
    
    """
