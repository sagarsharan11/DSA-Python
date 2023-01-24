# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Input: numRows = 1
# Output: [[1]]


### Brute Force Approach
# def generate(numRows):
#     lst = []
#     idx = 0
#     temp = 0
#     while idx!=numRows:
#         if idx == 0:
#             lst.append([1])
#         elif idx == 1:
#             lst.append([1,1])
#         else:
#             temp = lst[idx-1]
#             newLst = []
#             for i in range(idx+1):
#                 if i==0:
#                     newLst.append(1)
#                 elif i==idx:
#                     newLst.append(1)
#                 else:
#                     newLst.append(temp[i-1]+temp[i])
#             lst.append(newLst)
#         idx+=1
#     return lst
### TC: O(n^2)


### Optimimzed Approach
def generate(numRows):
    def helper(numRows):
        if numRows:
            helper(numRows-1)                 # generate above row first
            ans.append([1]*numRows)           # insert current row into triangle
            for i in range(1, numRows-1):     # update current row values using above row
                ans[numRows-1][i] = ans[numRows-2][i] + ans[numRows-2][i-1]
    ans = []
    helper(numRows)
    return ans



if __name__ == "__main__":
    numRows = 5
    print(generate(numRows))

    numRows = 1
    print(generate(numRows))