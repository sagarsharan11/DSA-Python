# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Input: temperatures = [30,60,90]
# Output: [1,1,0]

# Input: temperatures = [55,38,53,81,61,93,97,32,43,78]
# Output:               [ 3, 1, 1, 2, 1, 1, 0, 1, 1, 0]

# Input: temperatures = [77,77,77,77,77,41,77,41,41,77]
# Output:               [ 0, 0, 0, 0, 0, 1, 0, 2, 1, 0]


### Time Limit Exceeded for certain inputs | Working on another | O(n^2)
# def dailyTemperatures(temperatures):
#     answer = []
#     for i in range(len(temperatures)):
#         counter = 0
#         temp = temperatures[i]
#         if i+1 < len(temperatures):
#             for j in temperatures[i+1:]:
#                 counter = counter + 1
#                 if j > temp:
#                     answer.append(counter)
#                     break
#                 if len(temperatures[i+1:])==1:
#                     answer.append(0)
#                     break
#                 if len(temperatures[i+1:]) == counter:
#                     answer.append(0)
#         else:
#             answer.append(0)
#     return answer


### Another Approach using for and while loop: ----->>> Still exceeding the time limit
# def dailyTemperatures(temperatures):
#     answer = []
#     for i in range(len(temperatures)):
#         counter = 0
#         temp = temperatures[i]
#         temp_lst = temperatures[i+1:]
#         while counter < len(temp_lst):
#             temp2 = temp_lst[counter]
#             counter = counter + 1
#             if temp2 > temp:
#                 answer.append(counter)
#                 break
#             if len(temp_lst)==1:
#                 answer.append(0)
#                 break
#             if len(temp_lst) == counter:
#                 answer.append(0)
#     answer.append(0)
#     return answer

### Optimal Approach --- Using the Array | Stack | Monotonic Stack
def dailyTemperatures(temperatures):
    if len(temperatures) <= 1:
        return [0]
    stack = [len(temperatures)-1]
    ans = [0]
    for pos in range(len(temperatures)-2, -1, -1):
        while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[pos]:
            stack.pop()
        if len(stack) == 0:
            ans.append(0)
        else:
            ans.append(stack[-1]-pos)
        stack.append(pos)
    ans.reverse()
    return ans


if __name__=="__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    print(dailyTemperatures(temperatures))

    temperatures = [30,40,50,60]
    print(dailyTemperatures(temperatures))

    temperatures = [30,60,90]
    print(dailyTemperatures(temperatures))

    temperatures = [55,38,53,81,61,93,97,32,43,78]
    print(dailyTemperatures(temperatures))

    temperatures = [77,77,77,77,77,41,77,41,41,77]
    print(dailyTemperatures(temperatures))
