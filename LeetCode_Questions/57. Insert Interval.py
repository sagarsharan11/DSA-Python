# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


### Brute Force Approach
def insert(intervals, newInterval):
    result = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            result.append(newInterval)
            return result + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    result.append(newInterval)
    return result



if __name__ == "__main__":
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(insert(intervals, newInterval))

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print(insert(intervals, newInterval))