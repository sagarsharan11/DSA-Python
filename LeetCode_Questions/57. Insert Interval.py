# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


### Brute Force Approach
# def insert(intervals, newInterval):
    # result = []
    # for i in range(len(intervals)):
    #     if newInterval[1] < intervals[i][0]:
    #         result.append(newInterval)
    #         return result + intervals[i:]
    #     elif newInterval[0] > intervals[i][1]:
    #         result.append(intervals[i])
    #     else:
    #         newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    # result.append(newInterval)
    # return result

### Another Approach
def insert(intervals, newInterval):
    start, end = newInterval[0], newInterval[1]
    left = [i for i in intervals if i[1] < start]
    right = [i for i in intervals if i[0] > end]
    if left + right != intervals:
        start = min(start, intervals[len(left)][0])
        end = max(end, intervals[~len(right)][1])
    return left + [[start, end]] + right





if __name__ == "__main__":
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(insert(intervals, newInterval))

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print(insert(intervals, newInterval))