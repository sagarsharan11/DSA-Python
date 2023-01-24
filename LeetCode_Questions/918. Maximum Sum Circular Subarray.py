# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.

# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.


# def maxSubarraySumCircular(nums):
#     nums_2d = [[] for _ in range(len(nums))]
#     for i in range(len(nums)):
#         nums_2d[i].append(i)
#         nums_2d[i].append(nums[i])
#     nums_2d.sort(key=lambda x: x[1], reverse=True)

#     idx = 0
#     sum = 0

#     while sum <= sum + nums_2d[idx][1]:
#         sum = sum + nums_2d[idx][1]
#         idx += 1
    
#     return sum

### Optimal Approach
def maxSubarraySumCircular(nums):
    if len(nums) == 0:
        return 0
    maxTotal,maxSoFar,minSoFar,minTotal,s = nums[0], nums[0], nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        maxSoFar = max(nums[i], maxSoFar + nums[i])
        maxTotal = max(maxTotal, maxSoFar)            
        
        minSoFar = min(nums[i], minSoFar + nums[i])            
        minTotal = min(minTotal, minSoFar)            
        s += nums[i]
    if(s == minTotal):
        return maxTotal
    
    return max(s - minTotal, maxTotal)


if __name__ == "__main__":
    nums = [1,-2,3,-2]
    print(maxSubarraySumCircular(nums))

    nums = [5,-3,5]
    print(maxSubarraySumCircular(nums))

    nums = [-3,-2,-3]
    print(maxSubarraySumCircular(nums))