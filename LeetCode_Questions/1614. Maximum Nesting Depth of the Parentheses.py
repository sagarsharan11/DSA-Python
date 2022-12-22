# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation: Digit 8 is inside of 3 nested parentheses in the string.

# Input: s = "(1)+((2))+(((3)))"
# Output: 3


### Basic Approach
# def maxDepth(s):
#     max_count = 0
#     count = 0
#     for i in range(len(s)):
#         if s[i] == '(':
#             count += 1        
#             max_count = max(max_count, count)
#         elif s[i] == ')':
#            count -= 1
#     return max_count

### Using Stack
from collections import deque
def maxDepth(s):
    max_count = 0
    count = 0
    stack = deque()
    for i in range(len(s)):
        if s[i] == '(':
            count += 1        
            max_count = max(max_count, count)
        elif s[i] == ')':
           count -= 1
    return max_count



if __name__=="__main__":
    s = "(1+(2*3)+((8)/4))+1"
    print(maxDepth(s))

    s = "(1)+((2))+(((3)))"
    print(maxDepth(s))
