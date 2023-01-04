# Input: tasks = [2,2,3,3,2,4,4,4,4,4]
# Output: 4
# Explanation: To complete all the tasks, a possible plan is:
# - In the first round, you complete 3 tasks of difficulty level 2. 
# - In the second round, you complete 2 tasks of difficulty level 3. 
# - In the third round, you complete 3 tasks of difficulty level 4. 
# - In the fourth round, you complete 2 tasks of difficulty level 4.  
# It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.


# Input: tasks = [2,3,3]
# Output: -1
# Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.


#### Approach
"""
1. for -> len(tasks)
2. temp = 0 -> to store prev val; count = 0 -> to count the minRounds;
    diff = 0 -> to keep the diff if any in the curr iteration; valCount = 0 -> to keep the prev val count
3. if valCount >= 2 or 3 | then return break it in iterations of 2 or 3.....
4. if diff != 0, that is carried into next itertion
5. if valCount < 2, return -1
"""


def minimumRounds(tasks):
    idx = 0
    diff_dict = {}

    while idx < len(tasks):
        currDiff = tasks[idx]
        if currDiff not in diff_dict:
            valCount = 1
            diff_dict.update({currDiff:valCount})
        else:
            valCount = diff_dict[currDiff] + 1
            diff_dict.update({currDiff:valCount})
        idx+=1

    output = 0
    for difi in diff_dict:
        valCount = diff_dict[difi]
        if valCount == 1:
            return -1
        output += diff_dict[difi]//3 + bool(diff_dict[difi]%3)
    
    return output



if __name__ == "__main__":
    tasks = [2,2,3,3,2,4,4,4,4,4]
    print(minimumRounds(tasks))

    tasks = [2,3,3]
    print(minimumRounds(tasks))