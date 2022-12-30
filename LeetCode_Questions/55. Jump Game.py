# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

def canJump(nums):
    val = nums[0]
    if val > len(nums):
        return False
    else:
        idx = val - 1
        newNums = nums[idx:]
        newVal = newNums[0]
        if newVal > len(newNums):
            return False
        newIdx = 0
        while newIdx < len(nums):
            newIdx += val - 1 + newVal
            if newIdx == len(nums)-1:
                return True
            elif (newIdx < 0)  or (newIdx == 1):
                return True
            elif (newIdx == 0):
                return False
        return False

# Approach 1: Backtracking

# Approach 2: Dynamic Programming Top-down

# Approach 3: Dynamic Programming Bottom-up

# Approach 4: Greedy


if __name__ == '__main__':
    nums = [2,3,1,1,4]
    print(canJump(nums))

    nums = [3,2,1,0,4]
    print(canJump(nums))

    nums = [0]
    print(canJump(nums))

    nums = [1]
    print(canJump(nums))

    nums = [0,1]
    print(canJump(nums))

    nums = [0,2,3]
    print(canJump(nums))
