#  Input: nums = [2,5,3,9,5,3]
# Output: 3
# Explanation:
# - The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
# - The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
# - The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
# - The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
# - The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
# - The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
# The average difference of index 3 is the minimum average difference so return 3.


# Input: nums = [0]
# Output: 0
# Explanation:
# The only index is 0 so return 0.
# The average difference of index 0 is: |0 / 1 - 0| = |0 - 0| = 0.


# def minimumAverageDifference(nums):
#     numlen = len(nums)
#     idx_dict = {}
#     a = 0
#     for i in range(numlen):
#         b=0
#         a = (a + nums[i])
#         counter = i+1
#         try:
#             A = int(round(a/counter,3))
#         except ZeroDivisionError:
#             A = 0
#         while counter<numlen:
#             b = (b + nums[counter])
#             counter+=1
#         try:
#             B = int(round(b/(numlen-i-1),3))
#         except ZeroDivisionError:
#             B = 0
#         diff = abs(A-B)
#         if diff not in idx_dict:
#             idx_dict.update({diff:[i]})
#         elif diff in idx_dict:
#             val = idx_dict[diff]
#             val.append(i)
#             idx_dict.update({diff:val})
#     idx = min(idx_dict[min(idx_dict.keys())])
#     return idx

# ### Trying the Optimal Approach as Time Limit exceeds
# def minimumAverageDifference(nums):
#     numlen = len(nums)
#     idx_dict = {}
#     for i in range(numlen):
#         counter = i+1
#         a = sum(nums[:counter])
#         b = sum(nums[counter:])
#         try:
#             A = int(round(a/counter,3))
#         except ZeroDivisionError:
#             A = 0
#         try:
#             B = int(round(b/(numlen-i-1),3))
#         except ZeroDivisionError:
#             B = 0
#         diff = abs(A-B)
#         if diff not in idx_dict:
#             idx_dict.update({diff:[i]})
#         elif diff in idx_dict:
#             val = idx_dict[diff]
#             val.append(i)
#             idx_dict.update({diff:val})
#     idx = min(idx_dict[min(idx_dict.keys())])
#     return idx

#### Work on another approach beacause Time Limit still exceeds |||
### Using PREFIX SUM ARRAY
def minimumAverageDifference(nums):
    numlen = len(nums)
    prefixArr = [0]
    suffixArr = [sum(nums)]
    
    for i in range(numlen):
        prefix_val = nums[i] + prefixArr[i]
        prefixArr.append(prefix_val)

        suffix_val = suffixArr[i] - nums[i]
        suffixArr.append(suffix_val)

    idx_dict = {}
    for i in range(numlen):
        left_counter = i+1
        right_counter = numlen-i-1
        try:
            left_val = int(round(prefixArr[i+1]/left_counter,3))
        except ZeroDivisionError:
            left_val = 0
        try:
            right_val = int(round(suffixArr[i+1]/right_counter,3))
        except ZeroDivisionError:
            right_val = 0
        diff = abs(left_val-right_val)
        
        if diff not in idx_dict:
            idx_dict.update({diff:[i]})
        elif diff in idx_dict:
            val = idx_dict[diff]
            val.append(i)
            idx_dict.update({diff:val})
    idx = min(idx_dict[min(idx_dict.keys())])
    return idx


if __name__=='__main__':
    nums = [2,5,3,9,5,3]
    print(minimumAverageDifference(nums))

    nums = [0]
    print(minimumAverageDifference(nums))

    nums = [0,0,0,0,0]
    print(minimumAverageDifference(nums))