# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).


# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.


""" 
9.55 - 10:25
Approach:
1. Merge Sort
2. Divide the list repeatedly and call the mergesort function for each half | base case len(L) = 1 return
3. call mergeSort(L) -> mergeSort(R) | DIVIDE
4. i = j = k = 0
5. while L[i] < R[j]
"""

## For sorting in ascending order
# def sortArray(nums):
#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             if nums[i] > nums[j]:
#                 temp = nums[i]
#                 nums[i] = nums[j]
#                 nums[j] = temp
#     return nums
### this is brute force O(n^2)

### Working on the OPTIMIZED Approach
def sortArray(nums):
    def mergesort(A):
        LA = len(A)
        if LA == 1: return A
        LH, RH = mergesort(A[:LA//2]), mergesort(A[LA//2:])
        return merge(LH,RH)

    def merge(LH, RH):
        LLH, LRH = len(LH), len(RH)
        S, i, j = [], 0, 0
        while i < LLH and j < LRH:
            if LH[i] <= RH[j]: i, _ = i + 1, S.append(LH[i])
            else: j, _ = j + 1, S.append(RH[j])
        return S + (RH[j:] if i == LLH else LH[i:])
    
    return mergesort(nums)

if __name__ == "__main__":
    nums = [5,2,3,1]
    print(sortArray(nums))

    nums = [5,1,1,2,0,0]
    print(sortArray(nums))

